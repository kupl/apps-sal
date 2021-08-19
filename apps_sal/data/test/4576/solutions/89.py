a = int(input())
b = int(input())
c = int(input())
x1 = int(input())
x2 = 0
ans = 0
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            x2 = 500 * i + 100 * j + 50 * k
            if x2 == x1:
                ans += 1
print(ans)
