N, K = [int(n) for n in input().split()]
R, S, P = [int(n) for n in input().split()]
T = list(input())

p = {'r':R, 's':S, 'p':P}
cnv = {'r': 'p', 's': 'r', 'p': 's'}

score = 0
human = [0] * N

for i in range(K):
    human[i] = cnv[T[i]]
    score += p[human[i]]

for i in range(K, N):
    #human[i] = cnv[T[i]]
    if human[i - K] == cnv[T[i]]:
        #human[i] = T[i]
        continue
    else:
        human[i] = cnv[T[i]]
        score += p[human[i]]

print(score)

