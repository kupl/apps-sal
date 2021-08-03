N = int(input())
As = list(map(int, input().split()))

ansList = []
ans_1 = 0
for i in range(N):
    ans_1 += As[i] * (-1) ** i

ansList.append(ans_1)

for A in As[:-1]:
    ansList.append(2 * A - ansList[-1])

print(' '.join(map(str, ansList)))
