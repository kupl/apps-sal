N, K = map(int, input().split())
A = [int(x) for x in input().split()]
A.sort()
cards = 0
tail = N
needs = N
while tail:
    for i in range(tail):
        if A[i] + cards >= K:
            cards += A[i - 1]
            tail = i - 1
            needs = i
            break
    else:
        cards += A[i]
        tail = i
print(needs)
