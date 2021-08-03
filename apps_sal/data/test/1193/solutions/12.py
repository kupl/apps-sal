n, k = map(int, input().split())
S = list(map(int, input().split()))
S.sort(reverse=True)
print(S[k - 1])
