K = int(input())


cnt = 0
ans = ""


def dfs(n_str, digit):
    nonlocal cnt, ans
    if len(n_str) >= digit:
        cnt += 1
        if cnt == K:
            ans = n_str
        return
    last = int(n_str[-1])
    for i in range(max(0, last - 1), min(9, last + 1) + 1):
        dfs(n_str + str(i), digit)


digit = 1
while ans == "":
    for i in range(1, 10):
        dfs(str(i), digit)
    digit += 1
print(ans)
