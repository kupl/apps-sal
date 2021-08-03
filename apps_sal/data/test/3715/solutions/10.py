n = int(input())
a = list(map(int, input().split()))
cur = ans = 0
for i in a:
    if i == 0:
        cur = 0
        ans += 1
    if i == 1:
        if cur in (0, 1):
            cur = 2
        else:
            cur = 0
            ans += 1
    if i == 2:
        if cur in (0, 2):
            cur = 1
        else:
            cur = 0
            ans += 1
    if i == 3:
        cur = {0: 0, 1: 2, 2: 1}[cur]
print(ans)
