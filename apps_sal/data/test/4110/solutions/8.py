[D, G], *li = [list(map(int, i.split())) for i in open(0)]

ans = float('inf')


def dfs(i, ten, num, p):
    nonlocal ans
    if i == D:
        if ten >= G:
            ans = min(ans, num)
        else:
            for q in p:
                for r in range(li[q][0]):
                    ten += (q + 1) * 100
                    num += 1
                    if r == li[q][0]:
                        ten += li[q][1]
                    if ten >= G:
                        ans = min(ans, num)
                        break
                else:
                    continue
                break
    else:
        dfs(i + 1, ten + (i + 1) * 100 * li[i][0] + li[i][1], num + li[i][0], p)
        dfs(i + 1, ten, num, [i] + p)


dfs(0, 0, 0, [])
print(ans)
