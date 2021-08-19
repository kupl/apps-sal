import sys
# q=1
q = int(input())
for i in range(q):
    #n,m=[int(j) for j in sys.stdin.readline().split()]
    # n=int(sys.stdin.readline())
    a = [int(j) for j in sys.stdin.readline().split()]
    a.sort()
    if a[1] == a[2]:
        print('YES')
        print(a[0], a[0], a[2])
    else:
        print('NO')
