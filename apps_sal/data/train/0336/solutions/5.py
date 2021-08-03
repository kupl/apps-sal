class Solution:
    def minSteps(self, s: str, t: str) -> int:

        arr1 = defaultdict()
        arr2 = defaultdict()
        count = 0
        for i in range(len(s)):
            arr1[s[i]] = arr1.get(s[i], 0) + 1
            arr2[t[i]] = arr2.get(t[i], 0) + 1
        for i in range(len(t)):
            if t[i] not in arr1:
                count = count + arr2[t[i]]
                arr2[t[i]] = 0
                continue
            if arr2[t[i]] > arr1[t[i]]:
                count = count + arr2[t[i]] - arr1[t[i]]
                arr2[t[i]] = arr1[t[i]]
        return count
