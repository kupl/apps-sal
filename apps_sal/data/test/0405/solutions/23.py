import sys

n = int(input())
a = input()
if len(set(a)) == 1:
    print(n)
    return
res = 0
i = 0
while i < n and a[i] == '<':
    res += 1
    i += 1
i = n - 1
while i >= 0 and a[i] == '>':
    res += 1
    i -= 1
print(res)
