N = int(input())
L = list(map(int, input().split()))
c = 1
for l in L:
    if l == c:
        c += 1
r = N - c + 1
if r == N:
    print(-1)
else:
    print(r)
