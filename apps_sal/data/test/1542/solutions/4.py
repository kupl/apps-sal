import bisect
n = int(input())
x = [int(x) for x in input().split()]
q = int(input())
x.sort()
s = ''
for i in range(q):
    m = int(input())
    t = bisect.bisect(x, m)
    s += str(t) + '\n'
print(s)
