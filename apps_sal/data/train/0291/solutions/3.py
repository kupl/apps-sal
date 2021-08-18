class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        s = 0
        odd = {}
        ok = []
        even = {}
        ek = []
        for i in range(len(arr)):
            s += arr[i]
            if(s % 2 == 0):
                even[i] = s
                ek.append(i)
            else:
                odd[i] = s
                ok.append(i)
        j = 0
        c = 0
        for i in ok:
            while(j < len(ek) and ek[j] < i):
                j += 1
            c += j
        j = 0
        for i in ek:
            while(j < len(ok) and ok[j] < i):
                j += 1
            c += j

        return (c + len(ok)) % (10**9 + 7)
