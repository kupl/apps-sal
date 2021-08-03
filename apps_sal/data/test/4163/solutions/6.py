N = int(input())
3 <= N <= 100

D1_D2 = [map(int, input().split()) for _ in range(N)]
# print(D1_D2)
D1, D2 = [list(i) for i in zip(*D1_D2)]

right = int()

for s in range(0, N - 2):
    if D1[s] == D2[s] and D1[s + 1] == D2[s + 1] and D1[s + 2] == D2[s + 2]:
        right += 1

if right >= 1:
    print('Yes')
else:
    print('No')
