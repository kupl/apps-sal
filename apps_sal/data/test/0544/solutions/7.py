t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    ans = True
    for i in range(n // 2):
        if abs(ord(s[i]) - ord(s[n - i - 1])) not in (0, 2):
            ans = False
            break
    print('YES' if ans else 'NO')

