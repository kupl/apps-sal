A = []
for i in range(3):
    A += list(map(int, input().split()))
called = [False] * 9
bingo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
N = int(input())
for i in range(N):
    target = int(input())
    if target in A:
        called[A.index(target)] = True
for (a, b, c) in bingo:
    if called[a] and called[b] and called[c]:
        print('Yes')
        break
else:
    print('No')
