n = int(input())
p = set(tuple(map(int, input().split()))[1:])
q = set(tuple(map(int, input().split()))[1:])
a = p | q
if len(a) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
