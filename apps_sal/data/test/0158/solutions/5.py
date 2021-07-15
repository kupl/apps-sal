n = int (input())
a = sorted([int(i) for i in input().split()])
if a[n-1] < a[n]:
    print ('YES')
else:
    print ('NO')
