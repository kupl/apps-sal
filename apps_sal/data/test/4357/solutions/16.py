S = list(map(int, input().split()))
S.sort()
all = 0
all += S[0] + 10 * S[2] + S[1]
print(all)
