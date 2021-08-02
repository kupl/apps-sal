N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

diff = []
for i in H:
    diff.append(abs(A - T + i * 0.006))

diffmin = diff[0]
ans = 0
for i in range(N):
    if diffmin > diff[i]:
        diffmin = diff[i]
        ans = i
print(ans + 1)
