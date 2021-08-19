N = int(input())
a = [int(n) for n in input().split()]
i = 1
for j in range(N):
    if a[j] == i:
        i += 1
print(-1 if i == 1 else N - i + 1)
