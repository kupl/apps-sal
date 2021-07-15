S = list([ord(x) - ord('a') for x in list(input())])
N = int(input())
W = list(map(int, input().split()))
S = S + [W.index(max(W))] * N
print(sum([(i + 1) * W[v] for i, v in enumerate(S)]))

