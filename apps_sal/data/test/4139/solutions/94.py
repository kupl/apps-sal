N = int(input())


def dfs(keta, x):
    if x > N:
        return 0
    if keta == 9:
        three = 0
        five = 0
        seven = 0
        while x:
            if x % 10 == 3:
                three += 1
            elif x % 10 == 5:
                five += 1
            elif x % 10 == 7:
                seven += 1
            else:
                return 0
            x //= 10
        if three > 0 and five > 0 and seven > 0:
            return 1
    else:
        ans = 0
        x *= 10
        ans += dfs(keta + 1, x)
        ans += dfs(keta + 1, x + 3)
        ans += dfs(keta + 1, x + 5)
        ans += dfs(keta + 1, x + 7)
        return ans
    return 0


print(dfs(0, 0))
