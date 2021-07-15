h,w=map(int, input().split())
a=[i for i in [input() for _ in range(h)] if '#' in i]
b=[i for i in zip(*a) if '#' in i]
for i in zip(*b):
  print(''.join(i))
