s = input()
n = len(s)
for i in range(1, len(s) // 2):
    if s[:(n - 2 * i) // 2] == s[(n - 2 * i) // 2:n - 2 * i]:
        print(n - 2 * i)
        return
