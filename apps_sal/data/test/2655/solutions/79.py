N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

score = [A[0]]
for i in range(1, N):
    for j in range(2):
        score.append(A[i])

    if len(score) >= N:
        break

print((sum(score[:N-1])))

