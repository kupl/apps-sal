read = lambda: list(map(int, input().split()))
n = int(input())
a = list(read())
ans = -1
cnt = 0
for i in range(n):
    r = 0
    while a[i] % (2 ** r) == 0:
        r += 1
    r -= 1
    if r > ans:
        ans = r
        cnt = 1
    elif r == ans:
        cnt += 1
print(2 ** ans, cnt)
               

