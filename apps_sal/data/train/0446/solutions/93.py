class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        counts = defaultdict(list)
        for num, freq in list(c.items()):
            counts[freq].append(num)
        for freq in range(1, len(arr) + 1):
            while counts[freq] and k >= freq:
                del c[counts[freq].pop()]
                k -= freq
        return len(c)

