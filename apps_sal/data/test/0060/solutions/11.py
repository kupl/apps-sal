s = input()
n, c = int(s[:-1]), s[-1]
ans = (n - 1) // 4 * (12 + 4)
mp = {
    'a': 4,
    'b': 5,
    'c': 6,
    'd': 3,
    'e': 2,
    'f': 1
}
ans += mp[c]

n -= (n - 1) // 4 * 4

np = {
    1: 0,
    2: 7,
    3: 0,
    4: 7,
}

ans += np[n]

print(ans)
