from collections import deque

def z_sorted(a):
    a = deque(sorted(a))
    j = 0
    b = []
    
    while a:
        v = a.popleft() if (j%2 == 0) else a.pop()
        if j:
            if j%2 == 1:
                if v < b[-1]: return False
            else:
                if v > b[-1]: return False
        b.append(v)
        j += 1
    return b

def is_z_sorted(a):
    for i in range(len(a)):
        if i and i%2 == 1 and a[i] < a[i-1]: return False
        if i%2 == 0 and a[i] > a[i-1]: return False
    return True

def __starting_point():
    n = int(input())
    a = z_sorted([int(x) for x in input().split()])
    if a and is_z_sorted(a):
        print(' '.join(str(x) for x in a))
    else:
        print('IMPOSSIBLE')

__starting_point()
