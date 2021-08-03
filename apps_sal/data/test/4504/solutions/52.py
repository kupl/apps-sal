s = input()
n = len(s)
for i in range(2, n, 2):
    h = (n - i) // 2
    if s[:h] == s[h:n - i]:
        print(n - i)
        break
