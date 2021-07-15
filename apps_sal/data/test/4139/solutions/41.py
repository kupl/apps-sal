N = int(input())

dic = [3, 5, 7]

ans = set()
def dfs(s):
    if s:
        if int(s) <= N:
            if len(set(s)) == 3:
                ans.add(s)
        else:
            return
    for c in '753':
        dfs(s+c)

dfs("")
print((len(ans)))

