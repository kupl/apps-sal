n = int(input())
a = list(map(int, input().split()))
b = []
cur = -1
for i in a:
    if i == 1:
        if cur != -1:
            b.append(cur)
        cur = 0
    elif cur != -1:
        cur += 1
ans = 1
for i in b:
    ans *= i + 1
if cur == -1:
    ans = 0
print(ans)
