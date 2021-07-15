import heapq
class Heapq:
    def __init__(self, arr, desc=False):
        if desc:
            arr = [-a for a in arr]
        self.sign = -1 if desc else 1
        self.hq = arr
        heapq.heapify(self.hq)
 
    def pop(self):
        return heapq.heappop(self.hq) * self.sign
 
    def push(self, a):
        heapq.heappush(self.hq, a * self.sign)
 
    def top(self):
        return self.hq[0] * self.sign
        
N,M=list(map(int,input().split()))
A=list(map(int,input().split()))

q = Heapq(A, True)
    
for i in range(M):
    x=q.pop()
    q.push(x//2)

print((sum([q.pop() for _ in range(N)])))

