N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))
ans = 0
import bisect
b = []
for i in B:
    x = bisect.bisect_right(C,i)
    b.append(N-x)
y = sum(b)
c = [y]
for i in range(1,N):
    y -= b[i-1]
    c.append(y)
c.append(0)
for i in A:
    a = bisect.bisect_right(B,i)
    ans += c[a]
print(ans)
