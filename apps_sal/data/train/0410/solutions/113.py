class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        output = {}
        for i in range(lo,hi+1):
            a = i
            counter = 0
            while i > 1:
                if i%2 == 0:
                    i  = i/2
                else:
                    i = 3*i + 1
                counter += 1
            output[a] = counter
        output = sorted(output.items(), key=lambda x: x[1])
        return output[k-1][0]
