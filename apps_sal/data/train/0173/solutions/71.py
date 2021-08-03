class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        countMap = {}
        for i in range(len(arr)):
            arr[i] %= k
            countMap[arr[i]] = countMap.get(arr[i], 0) + 1
        print((countMap, arr))

        for char in arr:
            if char == 0:
                continue

            if k - char not in countMap:
                return False
            elif countMap[k - char] == 0:
                return False
            else:
                countMap[k - char] -= 1
        return True if (0 not in countMap or countMap[0] % 2 == 0) else False
