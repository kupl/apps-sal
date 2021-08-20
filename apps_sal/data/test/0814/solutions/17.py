input()
cs = list(map(int, input().split(' ')))
cs.sort()
print(' '.join([str(c) for c in cs]))
