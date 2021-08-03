import sys
s = input()
n = len(s)
for i in range(1, n - 1):
    if sorted([s[i - 1], s[i], s[i + 1]]) == ['A', 'B', 'C']:
        print('Yes')
        return
print('No')
