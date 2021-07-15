n = int(input())

A = set(list(map(int, input().split()))[1:])
B = set(list(map(int, input().split()))[1:])

if list(A | B) == list(range(1, n + 1)):
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
