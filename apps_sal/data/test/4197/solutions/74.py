n = int(input())
a = list(map(int, input().split()))
l = sorted([(a[i], i + 1) for i in range(n)])
c = [y for (x, y) in l]
print(' '.join(list(map(str, c))))
