class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        n = len(arr)
        mod_count = [0 for i in range(0, k)]

        for i in range(0, n):
            mod_count[arr[i] % k] += 1

        mid = int(k / 2)

        if(k % 2 == 1):
            if(mod_count[0] % 2 == 1):
                return False
        else:
            if(mod_count[0] % 2 == 1 or mod_count[mid] % 2 == 1):
                return False

        num = int((k - 1) / 2)

        for i in range(1, num + 1):
            if(mod_count[i] != mod_count[k - i]):
                return False

        return True
