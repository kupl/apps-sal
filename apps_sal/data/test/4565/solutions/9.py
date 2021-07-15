N = int(input())
S = list(input())

sum_W = [0]
for i in range(1, N):
    if S[i-1] == "W":
        sum_W.append(sum_W[i-1]+1)
    else:
        sum_W.append(sum_W[i-1])

sum_E = [S[1:].count("E")]
for i in range(0, N-1):
    if S[i+1] == "E":
        sum_E.append(sum_E[i]-1)
    else:
        sum_E.append(sum_E[i])

counts = []
for i in range(N):
    count = 0
    counts.append(sum_W[i]+sum_E[i])

print(min(counts))
