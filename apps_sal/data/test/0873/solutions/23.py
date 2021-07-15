n = int(input())
a = input()
b = input()
ans = 0
for i in range(len(a)):
    x = int(a[i])
    y = int(b[i])
    ans += min(abs(y - x), min(10 + x - y, 10 + y - x))
print(ans)
