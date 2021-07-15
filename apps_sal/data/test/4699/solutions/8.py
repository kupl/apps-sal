def dfs(A: list):
    if len(A) > len(str(n))+1:
        return
    if len(A) and (x := int("".join(A))) >= n and ans[0] > x:
        ans[0] = x
        return

    for v in d:
        if v == "0" and len(A) == 0:
            next
        A.append(v)
        dfs(A)
        A.pop()


n, k = list(map(int, input().split()))
d = sorted(list(set([str(i) for i in range(10)]) - set(input().split())))
ans = [10**10]
dfs([])
print((ans[0]))

