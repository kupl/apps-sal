def solve(n, t):
    m = 10 ** 10
    ans = 0
    s = '110' * n
    for i in range(3):
        if s[i:len(t) + i] == t:
            ans += (3 * m - i - n) // 3 + 1
    return ans


n = int(input())
t = input()
print(solve(n, t))
