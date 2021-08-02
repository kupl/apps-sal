q = int(input())
for i in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    if l1 == l2:
        print(l1 + 1, l2, end='\n')
    else:
        print(l1, l2, end='\n')
