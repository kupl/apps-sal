def f(t):
    return t.count('U') == t.count('D') and t.count('L') == t.count('R')
n, s = int(input()), input()
print(sum(f(s[i:j]) for i in range(n) for j in range(i + 1, n + 1)))
