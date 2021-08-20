(N, K) = map(int, input().split())
H = list(map(int, input().split()))
print(len(list(filter(lambda x: x >= K, H))))
