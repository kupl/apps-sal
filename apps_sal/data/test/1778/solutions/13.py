n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)

Ascore = 0
Bscore = 0

a = 0
b = 0

for i in range(n):
    if a == n:
        b += 1

    elif b == n:
        Ascore += A[a]
        a += 1

    elif A[a] > B[b]:
        Ascore += A[a]
        a += 1

    else:
        b += 1

    if b == n:
        a += 1

    elif a == n:
        Bscore += B[b]
        b += 1

    elif B[b] > A[a]:
        Bscore += B[b]
        b += 1

    else:
        a += 1

print(Ascore - Bscore)
