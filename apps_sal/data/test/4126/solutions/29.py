s = input()

n = len(s)
for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        print('No')
        return

n_left = int((n - 1) / 2)
for i in range(n // 4):
    if s[i] != s[n_left - 1 - i]:
        print('No')
        return

n_right = int((n + 3) / 2) - 1
for i in range(n // 4):
    if s[i + n_right] != s[n - 1 - i]:
        print('No')
        return

print('Yes')
