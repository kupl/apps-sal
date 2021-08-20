class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) == 1:
            return False
        arr = collections.Counter([i % k for i in arr])
        print(arr)
        i = 1
        j = k - 1
        while i <= j:
            if i == j:
                if arr[i] % 2 == 1:
                    return False
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        return True
