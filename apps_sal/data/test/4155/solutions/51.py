n = int(input())
h = list(map(int, input().split()))


def dfs(a):
    if not a:
        return 0
    cnt = 0
    while True:
        if 0 in a:
            z = [i for i, x in enumerate(a) if x == 0]
            cnt += dfs(a[:z[0]])
            for i in range(1, len(z)):
                cnt += dfs(a[z[i - 1] + 1:z[i]])
            cnt += dfs(a[z[-1] + 1:])
            return cnt
        else:
            a = [x - 1 for x in a]
            cnt += 1


print(dfs(h))
