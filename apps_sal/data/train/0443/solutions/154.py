class Solution:
    def numTeams(self, a: List[int]) -> int:
        greater, lesser = 0, 0
        c = 0
        n = len(a)
        for i in range(0, n):
            for j in range(i + 1, n):
                if(a[i] < a[j]):
                    greater = 0
                    lesser = 1
                elif(a[i] > a[j]):
                    lesser = 0
                    greater = 1
                else:
                    continue
                for k in range(j + 1, n):
                    if(a[j] < a[k] and lesser == 1):
                        c = c + 1
                    elif(a[j] > a[k] and greater == 1):
                        c = c + 1
        return c
