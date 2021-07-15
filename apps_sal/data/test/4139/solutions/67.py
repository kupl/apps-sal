n = int(input())

def dfs(cur, use, cnt):
    if cur > n:
        return
    if use == 0b111:
        cnt.append(1)

    dfs(cur*10+7, use|0b001, cnt)
    dfs(cur*10+5, use|0b010, cnt)
    dfs(cur*10+3, use|0b100, cnt)

cnt = []
dfs(0, 0, cnt)
print(len(cnt))
