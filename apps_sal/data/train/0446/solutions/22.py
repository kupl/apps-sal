class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1:
            return len(arr) - k

        counter = sorted(Counter(arr).values())
        print(counter)
        ptr = 0
        while k >= 0:
            k -= counter[ptr]
            ptr += 1
        
        return len(counter) - ptr + 1

