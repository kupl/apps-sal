t = list(map(int, input().split()))
n = t[0]
a = t[1]
b = t[2]
ans = 0
while a != b:
    n //= 2
    a = (a + 1) // 2
    b = (b + 1) // 2
    ans += 1
if n == 1:
    print('Final!')
else:
    print(ans)

