n = int(input())
L = list(map(int, input().split()))
x = sum(L)
x %= n + 1
ans = 0
for i in range(1, 6):
    if (x + i) % (n + 1) != 1:
        ans += 1
print(ans)
