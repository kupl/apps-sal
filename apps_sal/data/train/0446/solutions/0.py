class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = collections.Counter(arr)
        distinct = len(freq)
        freq_count = collections.Counter(list(freq.values()))
        idx = 1
        while k > 0:
            if k - idx * freq_count[idx] >= 0:
                k -= idx * freq_count[idx]
                distinct -= freq_count[idx]
                idx += 1
            else:
                return distinct - k // idx
        return distinct
