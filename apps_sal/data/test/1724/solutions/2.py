N = int(input())
data = [int(i) for i in input().split()]
M = input()
Sgood = [0] * N
Sgood[0] = max(data[0], 0)
for i in range(1, N):
    Sgood[i] = Sgood[i - 1] + max(data[i], 0)
Sorig = [0] * N
Sorig[0] = max(data[0] if M[0] == '1' else 0, 0)
for i in range(1, N):
    Sorig[i] = Sorig[i - 1] + max(data[i] if M[i] == '1' else 0, 0)
answer = Sorig[-1]
for i in range(1, N):
    if M[i] == '1':
        answer = max((answer, Sgood[i - 1] + Sorig[-1] - Sorig[i]))
print(answer)
