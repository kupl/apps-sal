N = int(input())
S = list(input())

ans = N

left_W = 0
right_E = S[1:].count("E")

for n in range(N):
    if n == 0:
        ans = min(ans, S[1:].count("E"))

    elif n == N - 1:
        ans = min(ans, S[:n].count("W"))

    else:
        if S[n] == "E":
            right_E -= 1
        if S[n - 1] == "W":
            left_W += 1
        ans = min(ans, left_W + right_E)

print(ans)
