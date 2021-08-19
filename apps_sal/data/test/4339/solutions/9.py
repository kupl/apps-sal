import bisect
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
lis = []
for i in range(N):
    lis.append(b[i] - a[i])
lis.sort()
ans = 0
sub = 0
for i in range(N):
    ns = a[i] - b[i]
    ans += bisect.bisect_left(lis, ns)
    if a[i] > b[i]:
        sub += 1
print((ans - sub) // 2)
