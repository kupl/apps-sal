import bisect
a = []
(n, h) = list(map(int, input().split()))
k = 0
for ai in input().split():
    bisect.insort(a, int(ai))
    if sum(a[::-2]) > h:
        break
    k += 1
print(k)
