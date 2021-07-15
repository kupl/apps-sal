N = int(input())
C = [0] * N
S = [0] * N
F = [0] * N

for i in range(N-1):
    C[i], S[i], F[i] = map(int, input().split())

def arrive(st):
    time = C[st] + S[st]
    for i in range(st + 1, N-1):
        if time <= S[i]:
            time = C[i] + S[i]
        else:
            if time % F[i] != 0:
                time = time + C[i] + (F[i] - time % F[i])
            else:
                time = time + C[i]
    return time

for i in range(N-1):
    print(arrive(i))
print("0")
