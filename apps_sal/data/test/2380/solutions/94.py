(N, M) = map(int, input().split())
A = list(map(int, input().split()))
cards = [list(map(int, input().split())) for _ in range(M)]
cards = sorted(cards, key=lambda x: x[1], reverse=True)
cnt = 0
for i in cards:
    A += [i[1]] * i[0]
    cnt += i[0]
    if cnt >= N:
        break
A.sort(reverse=True)
print(sum(A[:N]))
