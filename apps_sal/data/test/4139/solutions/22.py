n = int(input())
que = [3, 5, 7]
ans = 0


def dfs(s):
    nonlocal ans
    if n < s:
        return

    s = str(s)
    if "3" in s and "5" in s and "7" in s:
        ans += 1

    s = int(s)
    for i in que:
        dfs(10 * s + i)

    return ans


print((dfs(0)))
