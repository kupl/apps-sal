N, K = map(int, input().split())
rank = 1
S = K

while N >= S:
    rank += 1
    S *= K
#  print(S)

print(rank)
