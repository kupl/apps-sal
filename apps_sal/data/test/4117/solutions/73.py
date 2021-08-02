from sys import stdin
N = int(stdin.readline().rstrip())
L = sorted([int(_) for _ in stdin.readline().rstrip().split()])
ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if L[i] + L[j] > L[k] > L[j] > L[i]:
                ans += 1
print(ans)
