N = int(input())
S = [list(input().split()) for _ in range(N)]
for i in S:
    i[1] = 100 - int(i[1])
for i in range(N):
    S[i] += (i + 1,)
S.sort()
for i in S:
    print(i[2])
