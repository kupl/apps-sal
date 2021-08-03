N, M = map(int, input().split())
penalty = [0] * N
result = ["WA"] * N

for i in range(M):
    P, S = input().split()
    if S == "AC":
        result[int(P) - 1] = "AC"
    elif S == "WA" and result[int(P) - 1] == "WA":
        penalty[int(P) - 1] += 1
    else:
        continue

for j in range(N):
    if result[j] == "WA":
        penalty[j] = 0

print(result.count("AC"), sum(penalty))
