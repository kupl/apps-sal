n, m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]

if n == 1:
    ans = ["0"]
else:
    ans = list(str(10**(n - 1)))
check = [0] * n
for s, c in sc:
    s -= 1
    if check[s] == 0:
        ans[s] = str(c)
        check[s] = 1
    else:
        if ans[s] == str(c):
            continue
        print(-1)
        return
if n > 1 and ans[0] == "0":
    print(-1)
else:
    print("".join(ans))
