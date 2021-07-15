b, _ = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
if b % 2 == 0:
    a = a[-1:]
print('even' if sum(a) % 2 == 0 else 'odd')

