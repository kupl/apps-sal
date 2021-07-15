import collections
N,K = list(map(int,input().split()))
dic = {}
A = []
for _ in range(N):
    t,d = list(map(int,input().split()))
    A.append([t,d])
A.sort(key = lambda x:x[1], reverse = True)
val = 0
set_ = set()
duplicated = collections.deque([])
for t,d in A[:K]:
    val += d
    if t in set_:
        duplicated.append(d)
    else:
        set_.add(t)
now = val + len(set_)**2

nx = collections.deque(A[K:])
ans = now
c = len(set_)
while len(set_) < K and nx:
    i,j = nx.popleft()
    if i in set_:
        continue
    d = duplicated.pop()
    diff = j-d + 2*c+1
    set_.add(i)
    now += diff
    ans =max(ans,now)
    c += 1
print(ans)

