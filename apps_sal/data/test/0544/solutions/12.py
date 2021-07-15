from collections import defaultdict
t = int(input())
a = 'abcdefghijklmnopqrstuvwxyz'
changes = defaultdict(set)
changes['a'].add('b')
changes['z'].add('y')
for i in range(1,25):
    o1,o2 = a[i-1],a[i+1]
    changes[a[i]].add(o1)
    changes[a[i]].add(o2)
for _ in range(t):
    n = int(input())
    s = input()
    half = n//2
    for x in range(half):
        left = s[x]
        right = s[n-x-1]
        choice_left = changes[left]
        choice_right = changes[right]
        if not choice_left & choice_right:
            print ('NO')
            break
    else:
        print ('YES')

