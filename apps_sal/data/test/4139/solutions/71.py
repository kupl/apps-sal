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
    dfs(s+"3")
    dfs(s+"5")
    dfs(s+"7")

dfs("")
print(len(ans))
