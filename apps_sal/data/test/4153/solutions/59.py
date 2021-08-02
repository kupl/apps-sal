import collections
S = list(str(input()))
cc = collections.Counter(S)
ans = min(cc['0'], cc['1'])
print(ans * 2)
