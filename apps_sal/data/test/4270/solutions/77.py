n = int(input())
L = sorted(list(map(int, input().split())))
ans = (L[0] + L[1]) / 2
for i in range(2, n):
    ans = (ans + L[i]) / 2
print(ans)
