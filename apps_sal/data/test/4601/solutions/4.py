(n, k) = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort(reverse=True)
if k >= n:
    print(0)
else:
    for i in range(k):
        l[i] = 0
    print(sum(l))
