N, K = list(map(int, input().split()))
H = sorted(list(map(int, input().split())), reverse=True)[K:]

print((sum(H)))
