n = int(input())
a = [int(t) for t in input().split()]

if len(set(a)) > 3:
    print(-1)
    return
    
if len(set(a)) == 1:
    print(0)
    return
    
if len(set(a)) == 2:
    c = abs(list(set(a))[0] - list(set(a))[1])
    if c % 2 == 0:
        print(c // 2)
    else:
        print(c)
    return
    
a, b, c = sorted(list(set(a)))

if c - b != b - a:
    print(-1)
else:
    print(c - b)


