import math
import time


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        links = {}
        original_nums = set(A)

        def get_factors(n):
            out = []
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    out.append(i)
                    out.append(n // i)
            return out

        for num in A:
            factors = get_factors(num)
            if num not in links:
                links[num] = [num]
            for x in factors:
                links[num].append(x)
                if x not in links:
                    links[x] = [num]
                else:
                    links[x].append(num)

        def search(start):
            if start in seen:
                return 1
            stack = [start]
            size = 0
            while(stack):
                cur = stack.pop()
                seen.add(cur)
                if cur in original_nums:
                    size += 1
                for node in links[cur]:
                    if node not in seen:
                        stack.append(node)
                        seen.add(node)

            return size

        largest = 0
        seen = set()
        for num in A:
            res = search(num)
            largest = max(largest, res)

        return largest
