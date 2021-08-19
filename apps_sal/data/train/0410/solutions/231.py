import heapq


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        q = []
        for num in range(lo, hi + 1):
            count = 0
            tmp = num
            while num != 1:
                if num not in memo:
                    if num % 2 == 0:
                        cal = num // 2
                    else:
                        cal = 3 * num + 1
                    memo[num] = cal

                num = memo[num]
                count += 1

            heapq.heappush(q, (count, tmp))

        while k > 0:
            item = heapq.heappop(q)
            # print(item)
            k -= 1
        return item[1]
