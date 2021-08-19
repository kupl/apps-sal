def check(s):
    ss = 'ACTG'
    ans = 0
    for i in range(4):
        x = abs(ord(s[i]) - ord(ss[i]))
        ans += min(x, 26 - x)
    return ans


n = int(input())
s = input()
ma = 10 ** 9
for i in range(n - 3):
    ma = min(ma, check(s[i:i + 4]))
print(ma)
