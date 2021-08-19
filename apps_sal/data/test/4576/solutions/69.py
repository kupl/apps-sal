a = int(input())
b = int(input())
c = int(input())
x = int(input())
ans = 0
for i in range(a + 1):
    for j in range(b + 1):
        if (x - (500 * i + 100 * j)) % 50 == 0 and (x - (500 * i + 100 * j)) // 50 <= c and (500 * i + 100 * j <= x):
            ans += 1
print(ans)
