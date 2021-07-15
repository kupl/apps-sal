import collections
w = list(str(input()))
l = collections.Counter(w)
s = set(w)

for i in s:
    if int(l[i])%2 != 0:
        print('No')
        break
else:
    print('Yes')

