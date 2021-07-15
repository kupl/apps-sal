class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = defaultdict(lambda : 0)
        for i in arr:
            freq[i] += 1
        tup = []
        for i in freq:
            tup.append((freq[i], i))
        tup = sorted(tup)
        count = len(freq)
        
        for i in tup:
            k -= i[0]
            if k < 0:
                break
            count -= 1
        return count

