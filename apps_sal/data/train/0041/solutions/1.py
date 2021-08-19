t = int(input())
for test_i in range(t):
    (n, k) = map(int, input().split())
    s = list(input())
    ans = []
    for i in range(k - 1):
        if s[2 * i] != '(':
            i0 = s.index('(', 2 * i)
            ans.append((2 * i + 1, i0 + 1))
            (s[2 * i], s[i0]) = ('(', ')')
        if s[2 * i + 1] != ')':
            i0 = s.index(')', 2 * i + 1)
            ans.append((2 * i + 2, i0 + 1))
            (s[2 * i + 1], s[i0]) = (')', '(')
    for i in range(n // 2 - k + 1):
        if s[2 * (k - 1) + i] != '(':
            i0 = s.index('(', 2 * (k - 1) + i)
            ans.append((2 * (k - 1) + i + 1, i0 + 1))
            (s[2 * (k - 1) + i], s[i0]) = ('(', ')')
    print(len(ans))
    for pair in ans:
        print(*pair)
