N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

trans = {'r': 'p', 's': 'r', 'p': 's'}
score = {'r': R, 's': S, 'p': P, 't': 0}

a = [trans[t] for t in T]

for i in range(K, N):
    if a[i] == a[i - K]:
        a[i] = 't'
print(sum([score[s] for s in a]))
