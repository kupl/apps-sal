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

        # start_time = time.time()

        for num in A:
            factors = get_factors(num)
            if num not in links:
                links[num] = [num]
            for x in factors:
                # if num not in links:
                #     links[num] = [x]
                # else:
                links[num].append(x)
                if x not in links:
                    links[x] = [num]
                else:
                    links[x].append(num)

        # print(time.time()-start_time)

        def search(start):
            if start in seen:
                return 1
            stack = [start]
            size = 0
            while(stack):
                cur = stack.pop()
                # print(cur)
                seen.add(cur)
                if cur in original_nums:
                    size += 1
                # print(cur)
                for node in links[cur]:
                    if node not in seen:
                        stack.append(node)
                        seen.add(node)

            return size

        largest = 0
        seen = set()
        # print(original_nums)
        # print(links)
        for num in A:
            res = search(num)
            largest = max(largest, res)

        # print(time.time()-start_time)
        return largest
