N, D, A = map(int, input().split())

Monster = [0]*N
for i in range(N):
    Monster[i] = list(map(int, input().split()))

Monster.sort(key=lambda x:x[0])

from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort

from collections import deque

d = deque()
damage = 0
ans = 0
for i in range(N):
    while len(d)>0:
        a = d.popleft()
        if a[0]==i:
            damage -= a[1]
        else:
            d.appendleft(a)
            break
    Monster[i][1] -= damage
    count = -(-max(Monster[i][1],0)//A)
    ans += count
    right = Monster[i][0]+2*D
    ind = bisect(Monster,[right,10**9+1])
    damage += A*count
    d.append([ind,A*count])
print(ans)
