s = input()
n = len(s)

for i in range(1, n):
    if (n - i) % 2 == 0:
        m = (n - i) // 2
        if s[0:m] == s[m:n - i]:
            print(n - i)
            return
