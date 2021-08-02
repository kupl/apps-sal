n, k = list(map(int, input().split()))
l = sorted([list(map(int, input().split()))for i in range(n)])
for a, b in l:
    k -= b
    if k < 1:
        print(a)
        break
