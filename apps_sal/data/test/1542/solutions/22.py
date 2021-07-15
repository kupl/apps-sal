import bisect

n = int(input())
x = list(map(int, input().split()))
x.sort()
q = int(input())
a = []
for i in range(q):
    v = int(input())
    i = bisect.bisect_right(x, v)
    print(i)

