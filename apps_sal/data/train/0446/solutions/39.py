class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        import heapq

        vals = {}

        for val in arr:
            if val in vals:
                vals[val] += 1
            else:
                vals[val] = 1

        hp = []
        for val in vals:
            hp.append(vals[val])

        heapq.heapify(hp)

        # count represents the number of elements popped
        while(k > 0 and len(hp)):
            curr = heapq.heappop(hp)
            if curr <= k:
                k = k - curr
            else:
                k = curr - k
                heapq.heappush(hp, k)
                break
        return len(hp)
