
import math
import bisect

class Fenwick:
    def __init__(self, n):
        self.data = [[0,0] for i in range(n)] 
    
    def update(self, pos, dist):
        while pos<len(self.data):
            self.data[pos][0] += 1
            self.data[pos][1] += dist
            pos = pos | (pos+1)
    
    def query(self, pos):
        ans = [0,0]
        while pos > 0:
            ans[0] += self.data[pos-1][0]
            ans[1] += self.data[pos-1][1]
            pos = pos & (pos-1)
        return ans


def rints():
    return list(map(int,input().split()))


n = int(input())

x = rints()
v = rints()

ascDist = list(range(n))
ascDist.sort(key=lambda i: x[i])

uniqueSpeeds = sorted(list(set(v)))

tree = Fenwick(len(uniqueSpeeds))


ans = 0
for i in ascDist:
    speedId = bisect.bisect_left(uniqueSpeeds, v[i])
    count, dsum = tree.query(speedId+1)
    ans += count*x[i] - dsum
    tree.update(speedId, x[i])

print(ans)


