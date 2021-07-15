from collections import deque

N=int(input())
a=list(map(int,input().strip().split()))

b=deque()
for n in range(N):
    if n%2==0:
        b.append(a[n])
    else:
        b.appendleft(a[n])
ans=" ".join(list(map(str,b))) if n%2==1 else " ".join(list(map(str,list(deque(b))[::-1])))
print(ans)
