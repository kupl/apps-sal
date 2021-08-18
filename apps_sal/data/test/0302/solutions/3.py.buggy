ans = 1000000000000
mul = []


def dfs(now, num, opt):
    if num == 0:
        nonlocal ans
        ans = min(ans, opt)
        return
    if now == -1:
        return
    i = -10
    while i * mul[now] <= num:
        i += 1
    dfs(now - 1, num - (i - 1) * mul[now], opt + abs(i - 1) * (now + 1))
    dfs(now - 1, num - i * mul[now], opt + abs(i) * (now + 1))


def main():
    mul.append(int(1))
    num = int(input())
    for i in range(1, 18, 1):
        mul.append(mul[i - 1] * 10)
    for i in range(1, 18, 1):
        mul[i] += mul[i - 1]
    i = 1
    while mul[i] <= num:
        i += 1
    n = i
    dfs(n, num, 0)
    print(ans)


main()
