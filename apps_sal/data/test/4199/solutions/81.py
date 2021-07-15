N, K = map(int, input().split())
h = list(map(int, input().split()))

answer = sum(i >= K for i in h)

print(answer)
