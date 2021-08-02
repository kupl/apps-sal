N = int(input())
S = input()
r = 0
g = 0
b = 0
for i in range(N):
    if S[i] == "R":
        r += 1
    elif S[i] == "G":
        g += 1
    else:
        b += 1

ms = (N - 3) // 2
t = 0
for i in range(ms + 1):
    for j in range(N - (2 * i + 3) + 1):
        if S[j] != S[j + i + 1] and S[j] != S[j + 2 * i + 2] and S[j + i + 1] != S[j + 2 * i + 2]:
            t += 1

print(r * g * b - t)
