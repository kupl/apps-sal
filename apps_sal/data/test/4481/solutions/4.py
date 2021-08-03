import collections
n = int(int(input()))
a = [input() for i in range(n)]
m = collections.Counter(a).most_common()
print('\n'.join(sorted([a for a, b in m if b == m[0][1]])))
