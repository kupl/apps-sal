S = input().strip()
N = len(S)
A = []
cur = 0
for i in range(1, N):
    if S[i] == "R" and S[i - 1] == "L":
        x = S[cur:i]
        A.append((cur, x))
        cur = i
A.append((cur, S[cur:N]))
B = [0 for _ in range(N)]
while A:
    cur, x = A.pop()
    n = len(x)
    for i in range(1, n):
        if x[i] == "L" and x[i - 1] == "R":
            ind = i
            break
    if n % 2 == 0:
        B[cur + ind] = n // 2
        B[cur + ind - 1] = n // 2
    else:
        if ind % 2 == 0:
            B[cur + ind] = (n + 1) // 2
            B[cur + ind - 1] = n // 2
        else:
            B[cur + ind] = n // 2
            B[cur + ind - 1] = (n + 1) // 2
print(*B)
