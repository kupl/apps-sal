x, n = list(map(int, input().split()))
min = 105
ans = 105
if n != 0:
    p = list(map(int, input().split()))
    for i in range(102):
        if i not in p:
            if abs(i - x) < min:
                min = abs(i - x)
                ans = i
else:
    ans = x
print(ans)

