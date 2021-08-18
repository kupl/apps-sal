n, m = list(map(int, input().split()))

ans = [-1] * n
for i in range(m):
    s, c = list(map(int, input().split()))
    s -= 1
    if ans[s] != -1 and ans[s] != c:
        print((-1))
        return
    ans[s] = c

if n > 1 and ans[0] == 0:
    print((-1))
    return

if ans[0] == -1:
    if n == 1:
        ans[0] = 0
    else:
        ans[0] = 1
for i in range(1, n):
    if ans[i] == -1:
        ans[i] = 0
print((''.join(map(str, ans))))
