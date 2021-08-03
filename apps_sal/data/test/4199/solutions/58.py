n, k = list(map(int, input().split(' ')))
h = list(map(int, input().split(' ')))
print((sum(i >= k for i in h)))
