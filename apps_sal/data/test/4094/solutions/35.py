K = int(input())
a = 7
ans = -1
for i in range(K + 1):
    if a % K == 0:
        ans = i + 1
        break
    a = (a * 10 + 7) % K
print(ans)
