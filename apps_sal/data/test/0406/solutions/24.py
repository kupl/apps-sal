n = int(input())
a, b = 0, 0
ans = 0
for i in sorted(map(int, input().split()), reverse=True):
    if a == 0 or a > i + 1:
        a = i
    elif b == 0:
        a, b = 0, i
    else:
        ans += i * b
        a, b = 0, 0
print(ans)
