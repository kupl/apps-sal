N = int(input())
A1 = input().split(' ')
A2 = input().split(' ')
A1 = [int(A1[i]) for i in range(N)]
A2 = [int(A2[i]) for i in range(N)]
Saidai = 0
for i in range(N):
    Atai = 0
    for j in range(i + 1):
        Atai += A1[j]
    for h in range(i, N):
        Atai += A2[h]
    if Atai > Saidai:
        Saidai = Atai
print(Saidai)
