(h, w) = map(int, input().split())
a = [i for i in [input() for i in range(h)] if '#' in i]
a = [i for i in zip(*a) if '#' in i]
for i in zip(*a):
    print(''.join(i))
