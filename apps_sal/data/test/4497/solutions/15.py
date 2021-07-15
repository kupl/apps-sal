N = int(input())
ans = [1, 2, 4, 8, 16, 32, 64]
print(max(filter(lambda x : x<=N,ans)))
