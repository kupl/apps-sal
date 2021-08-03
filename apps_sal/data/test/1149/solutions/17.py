n = int(input())
s = set()
for i in range(2):
    p = [int(i) for i in input().split()]
    p.pop(0)
    s.update(set(p))
print('I become the guy.' if s == set(range(1, n + 1)) else 'Oh, my keyboard!')
