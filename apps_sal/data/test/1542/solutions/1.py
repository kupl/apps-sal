from bisect import bisect_right
n = int(input())
x = list(map(int, input().split()))
q = int(input())
x.sort()
for i in range(q):
    m = int(input())
    print(bisect_right(x, m))
