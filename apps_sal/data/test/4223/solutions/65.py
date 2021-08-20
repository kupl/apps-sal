import itertools
n = int(input())
s = input()
ans = ''
iter = itertools.groupby(s)
for (key, value) in iter:
    ans += key
print(len(ans))
