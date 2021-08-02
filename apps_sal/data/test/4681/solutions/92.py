n = int(input())
if n == 1:
    print(1)
    return
x = 2
y = 1
ans = 0
for i in range(n - 1):
    ans = x + y
    x = y
    y = ans
print(ans)
