h, w = map(int, input().split())
a = [i for i in [input() for _ in range(h)] if '
b = [i for i in zip(*a) if '
for i in zip(*b):
    print(''.join(i))
