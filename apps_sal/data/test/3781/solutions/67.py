t = int(input())
for _ in range(t):
    N = int(input())
    l = sorted(map(int, input().split()))
    if N % 2:
        print('Second')
    elif sum(l[::2]) == sum(l[1::2]):
        print('Second')
    else:
        print('First')
