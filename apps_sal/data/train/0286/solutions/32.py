class Solution:
    # Brute force: check all permutations
    # O(n! / (ball_count! ^ k)) time, O(n) space
    def getProbability(self, balls: List[int]) -> float:
        balls_flattened = []
        for i, count in enumerate(balls):
            balls_flattened.extend([i] * count)

        def has_same_distinct_color(perm):
            n = len(perm)
            return len(set(perm[: n // 2])) == len(set(perm[n // 2:]))

        total = [0]
        same_distinct_color = [0]

        def get_perm(cur, balls):
            if not balls:
                total[0] += 1
                same_distinct_color[0] += has_same_distinct_color(cur)
                return
            for i in range(len(balls)):
                if i > 0 and balls[i] == balls[i - 1]:
                    continue
                get_perm(cur + [balls[i]], balls[:i] + balls[i + 1:])

        get_perm([], balls_flattened)
        return same_distinct_color[0] / total[0]

    # Permutations of combinations
    # O(ball_count ^ k) time (put 0, 1, 2, ..., ball_count balls into box 1, and do it for k colors), O(k) space
    def getProbability(self, balls: List[int]) -> float:

        factorial_cache = [1]
        for i in range(1, sum(balls) + 1):
            factorial_cache.append(factorial_cache[-1] * i)

        def get_perm_count(arr):
            total = factorial_cache[sum(arr)]
            for a in arr:
                total //= factorial_cache[a]
            return total

        total_perms = get_perm_count(balls)
        valid_perms = [0]

        def find_valid_split(n, start, distinct1, group1, distinct2, group2):
            if n == 0:
                if distinct1 == distinct2:
                    valid_perms[0] += get_perm_count(group1) * get_perm_count(group2)
                return

            for i in range(start, len(group1)):
                if group1[i] == 0:
                    continue

                new_num1 = group1[i] - 1
                new_distinct1 = distinct1 if new_num1 > 0 else distinct1 - 1
                new_num2 = group2[i] + 1
                new_distinct2 = distinct2 if new_num2 > 1 else distinct2 + 1
                if new_distinct1 < new_distinct2:
                    continue

                new_group1 = group1[:i] + [new_num1] + group1[i + 1:]
                new_group2 = group2[:i] + [new_num2] + group2[i + 1:]
                find_valid_split(n - 1, i, new_distinct1, new_group1, new_distinct2, new_group2)

        find_valid_split(sum(balls) // 2, 0, len(balls), balls, 0, [0] * len(balls))
        return valid_perms[0] / total_perms
