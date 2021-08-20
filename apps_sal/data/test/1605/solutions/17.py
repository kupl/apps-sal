s = input()
d = dict()
d['a'] = [0, 0]
d['b'] = [0, 0]
odd = even = 0
for i in range(len(s)):
    d[s[i]][i & 1] += 1
    odd += d[s[i]][i & 1]
    even += d[s[i]][1 - i & 1]
print(even, odd)
