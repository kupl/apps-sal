n = int(input())
b = list(map(int, input().split()))
b.append(0)
ans = 0
for i in range(n):
    ans += abs(b[i] - b[i - 1])
print(ans)

