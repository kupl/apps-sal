(n, k) = list(map(int, input().split()))
h = list(map(int, input().split()))
print(sum((height >= k for height in h)))
