def solve(s, n):
    i = 0
    while i < n // 2:
        if s[i] != s[n - i - 1]:
            if abs(ord(s[i]) - ord(s[n - i - 1])) != 2:
                return "NO"
        i += 1
    return "YES"


for _ in range(int(input())):
    n = int(input())
    s = input()
    print(solve(s, n))
