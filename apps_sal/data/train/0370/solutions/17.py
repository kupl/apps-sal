class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def sieve():
            i = 2
            while i < len(spf):
                spf[i] = 2
                i += 2
            i = 3
            while i * i < len(spf):
                if spf[i] == i:
                    j = i
                    while j < len(spf):
                        if spf[j] == j:
                            spf[j] = i
                        j += i
                i += 2
        (spf, di, factors, visited_nums, visited_factors, ans) = ([i for i in range(max(A) + 1)], defaultdict(set), defaultdict(set), set(), set(), 1)
        sieve()
        for num in A:
            x = num
            while x != 1:
                di[spf[x]].add(num)
                factors[num].add(spf[x])
                x //= spf[x]
        for num in A:
            if num in visited_nums:
                continue
            visited_nums.add(num)
            (cur, queue) = (1, deque([]))
            for factor in factors[num]:
                queue.append(factor)
            while queue:
                factor = queue.popleft()
                visited_factors.add(factor)
                for next_num in di[factor]:
                    if next_num in visited_nums:
                        continue
                    visited_nums.add(next_num)
                    cur += 1
                    for next_factor in factors[next_num]:
                        if next_factor in visited_factors:
                            continue
                        visited_factors.add(next_factor)
                        queue.append(next_factor)
            ans = max(ans, cur)
        return ans
