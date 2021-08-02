from sys import exit, stdin, stderr


def rl():
    return [int(w) for w in stdin.readline().split()]


T, = rl()
for _ in range(T):
    n, = rl()
    s = stdin.readline().rstrip()
    l = 1
    while l < n and s[l] == s[0]:
        l += 1
    if l == n:
        print((n + 2) // 3)
        continue
    r = n
    while s[r - 1] == s[0]:
        r -= 1
    y = (n - r + l) // 3
    k = l
    for i in range(l, r):
        if s[i] != s[k]:
            y += (i - k) // 3
            k = i
    y += (r - k) // 3
    print(y)
