h, w = map(int, input().split())
a = [i for i in [input() for i in range(h)] if "
a = [i for i in zip(*a) if "
for i in zip(*a):
    print("".join(i))
