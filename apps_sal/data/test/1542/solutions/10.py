import bisect
n = int(input())
x = [int(x) for x in input().split()]
q = int(input())
x.sort()
for i in range(q):
    m = int(input())
    print(bisect.bisect_right(x, m))
