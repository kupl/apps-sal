import sys
readline = sys.stdin.readline

N = int(readline())
L = list(map(int, readline().split()))

L = sorted(L)

ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if len(set([L[i], L[j], L[k]])) != 3:
                continue
            if L[i] + L[j] > L[k]:
                ans += 1

print(ans)
