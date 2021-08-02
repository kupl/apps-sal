a = int(input())
b = int(input())
c = int(input())
x = int(input())
if x % 100 > 0 and c == 0:
    print((0))
    return
else:
    a = min(a, x // 500)
    b = min(b, x // 100)
    c = min(c, x // 50)
    ans = 0
    for i in range(a + 1):
        for j in range(b + 1):
            for c in range(c + 1):
                if i * 500 + j * 100 + c * 50 == x:
                    ans += 1
print(ans)
