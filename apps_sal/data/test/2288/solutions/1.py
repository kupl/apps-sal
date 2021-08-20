t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    if 0 < sum(b) < len(b):
        print('Yes')
    elif a == sorted(a):
        print('Yes')
    else:
        print('No')
