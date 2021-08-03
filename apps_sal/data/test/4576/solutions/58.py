def getints(): return map(int, input().split())


a = int(input())
b = int(input())
c = int(input())
x = int(input())
ans = 0
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            val = 500 * i + 100 * j + 50 * k
            if val == x:
                ans += 1
print(ans)
