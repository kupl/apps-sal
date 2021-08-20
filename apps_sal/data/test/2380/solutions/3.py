import sys
(N, M) = map(int, input().split())
A = list(map(int, input().split()))
card = [list(map(int, i.rstrip().split())) for i in sys.stdin.readlines()]
card = sorted(card, key=lambda x: x[1], reverse=True)
A = sorted(A)
i = 0
for (b, c) in card:
    for _ in range(b):
        if i >= N:
            break
        elif A[i] >= c:
            break
        else:
            A[i] = c
            i += 1
print(sum(A))
