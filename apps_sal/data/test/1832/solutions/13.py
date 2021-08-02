def solve():
    n = int(input())
    s = input().split()

    m = 0

    for i in range(len(s)):
        s[i] = int(s[i])
        m = max(m, s[i])
    print('a' * (m + 1))
    cur = ['a'] * (m + 1)
    for i in range(len(s)):
        if cur[s[i]] == 'a':
            cur[s[i]] = 'b'
        else:
            cur[s[i]] = 'a'
        print(''.join(cur))


t = int(input())

for i in range(t):
    solve()
