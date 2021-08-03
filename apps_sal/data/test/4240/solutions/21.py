s = input()
t = input()
n = len(s)
if s == t:
    print('Yes')
    return
for i in range(1, n):
    s = s[n - 1] + s[:n - 1]
    if s == t:
        print('Yes')
        return
print('No')
