from collections import deque

n,m = list(map(int, input().split()))
g = [[] for _ in range(n)]
prev = [0] * n

for i in range(m):
    a,b = list(map(int, input().split()))
    g[a-1].append(b)
    g[b-1].append(a)

count = 0
prev[0] = 1

def keiro(pre,q,now):
    nonlocal count
    if len(q) == 0:
            return

    now = q.popleft()
    
    for no in g[now-1]:
        if pre[no-1] == 0:

            pre_1 = pre.copy()
            pre_1[no-1] = 1
            if sum(pre_1) == n:
                count+=1
                return
            q.append(no)
            keiro(pre_1,q,no)
        else:

            keiro(pre,q,no)


keiro(prev,deque([1]),1)
print(count)


