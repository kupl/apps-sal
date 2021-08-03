import sys
def input(): return sys.stdin.readline().rstrip()


N, K = list(map(int, input().split()))

d = []
A = []

for i in range(K):
    x = int(input())
    d.append(x)
    a = list(map(int, input().split()))
    A.append(a)

vec = [0] * N

for a in A:
    for i in a:
        i -= 1
        vec[i] += 1

ans = 0
for i in range(N):
    if vec[i] == 0:
        ans += 1

print(ans)
