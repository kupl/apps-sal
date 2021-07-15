n = int(input())
L = list(map(int, input().split()))
a = 0
b = 0
for i in L:
    if i == 1:
        a += 1
    else:
        b += 1
if b <= a:
    ans = b
    a -= b
    b = 0
else:
    ans = a
    a = 0
    b -= 1
ans += a // 3
print(ans)

