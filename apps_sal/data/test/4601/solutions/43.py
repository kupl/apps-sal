H, K = [int(n) for n in input().split()]
H = [int(n) for n in input().split()]

print(sum(sorted(H, reverse=True)[K:]))
