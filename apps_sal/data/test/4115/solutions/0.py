s = input()
n = len(s) - 1
print(sum((s[i] != s[n - i] for i in range(n + 1))) // 2)
