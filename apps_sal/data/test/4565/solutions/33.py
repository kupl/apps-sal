N = int(input())
S = list(input())
directed = [S[1:].count("W")]

for i in range(1, len(S)):
    d = directed[i - 1]
    if S[i - 1] == "E":
        d += 1
    if S[i] == "W":
        d -= 1
    directed.append(d)

print(N - max(directed) - 1)
