(x, n) = list(map(int, input().split()))
p = list(map(int, input().split()))
ans = 0
for i in range(1, 102):
    if i not in list(p):
        if abs(x - i) < abs(x - ans):
            ans = i
print(ans)
