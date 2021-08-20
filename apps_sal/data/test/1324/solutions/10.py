import collections
a = tuple(map(int, str.split(input())))
ns = collections.Counter(list(map(int, str.strip(input()))))
print(sum([a[i - 1] * ns[i] for i in ns]))
