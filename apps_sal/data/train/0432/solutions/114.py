class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0 or len(nums) < k:
            return False
        from collections import Counter
        import heapq

        d = Counter(nums)
        num_groups = len(nums) // k
        h = [(i, c) for i, c in d.items()]
        heapq.heapify(h)

        while len(h) > 0:
            temp = []
            k_ = k
            while k_ > 0:
                if h:
                    x, c = heapq.heappop(h)
                    if temp:
                        if temp[-1] == x - 1:
                            temp.append(x)
                        else:
                            return False
                    else:
                        temp.append(x)
                else:
                    return False

                d[x] -= 1
                k_ -= 1
            print(temp)
            for x in temp:
                if d[x] > 0:
                    heapq.heappush(h, (x, d[x]))

        return True
