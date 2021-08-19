(N, K) = map(int, input().split())
num_list = list(map(int, input().split()))
print(sum(sorted(num_list, reverse=True)[:K]))
