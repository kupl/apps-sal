class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        import math

        def is_not_square(num):
            return int(math.sqrt(num) + 0.5) ** 2 != num

        memo = {}

        def perms(arr):
            key = tuple(sorted(arr))

            if key in memo:
                return memo[key]
            if len(arr) <= 1:
                return [arr]

            permutations = []
            seen = set()
            for i in range(len(arr)):
                el = arr[i]
                rest = arr[:i] + arr[i + 1:]
                # if all([is_not_square(el+n) for n in rest]): continue
                if el not in seen:
                    sub_perms = perms(rest)
                    if not sub_perms:
                        continue
                    for p in sub_perms:
                        if not is_not_square(el + p[0]):
                            permutations.append([el] + p)
                seen.add(arr[i])

            memo[key] = permutations
            return permutations

        return len(perms(A))
