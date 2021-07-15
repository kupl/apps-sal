import bisect
def dfs(cnt, s, three, five, seven):
    if cnt == 10:
        return
    if s != "" and min(three, five, seven) > 0:
        v.append(int(s))
    dfs(cnt+1, "3"+s, three+1, five, seven)
    dfs(cnt+1, "5"+s, three, five+1, seven)
    dfs(cnt+1, "7"+s, three, five, seven+1)


v = []
dfs(0, "", 0, 0, 0)
v.sort()

n = int(input())
print(bisect.bisect_right(v, n))
