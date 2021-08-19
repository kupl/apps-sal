def main():
    n, m = list(map(int, input().split()))
    ans = [0 for _ in range(n)]
    for _ in range(m):
        s, c = list(map(int, input().split()))
        if n > 1 and s == 1 and c == 0:
            return -1
        if s - 1 > n:
            return -1
        if ans[s - 1] == 0 or ans[s - 1] == c:
            ans[s - 1] = c
        else:
            return -1
    # if n == 1 and ans[0]==0:
    #     continue
    if n > 1 and ans[0] == 0:
        ans[0] = 1

    ans = int("".join(map(str, ans)))
    if len(str(ans)) < n:
        return -1
    return ans


def __starting_point():
    print((main()))


__starting_point()
