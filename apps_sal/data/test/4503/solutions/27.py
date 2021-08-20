(h, n) = map(int, input().split())
A = list(map(int, input().split()))
print('YNeos'[sum(A) < h::2])
