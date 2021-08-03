n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    x = a.pop()
    y = b.pop()
    if x <= y:
        ans += x
        y -= x
        if a[-1] > y:
            ans += y
            a[-1] -= y
        else:
            ans += a[-1]
            a[-1] = 0
    else:
        ans += y
print(ans)
