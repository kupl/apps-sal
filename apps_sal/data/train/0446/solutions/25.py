class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = {}
        for id in arr:
            counter[id] = counter.get(id, 0) + 1
        id2count = sorted([[count, id] for (id, count) in counter.items()], key=lambda x: (-x[0], x[1]))
        for i in range(len(id2count) - 1, -1, -1):
            count = id2count[i][0]
            if k - count < 0:
                break
            id2count.pop()
            k -= count
        return len(id2count)
