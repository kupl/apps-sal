import sys
input = sys.stdin.readline
N, C = map(int, input().split())

X = []

for i in range(N):
    x, c = map(int, input().split())
    X.append((x, c))

PS1 = [[0, 0, 0]]
PS2 = [[0, 0, 0]]
QS1 = [[0, 0, 0]]
QS2 = [[0, 0, 0]]


for i in range(N):
    c1, xx, c0 = PS1[i]
    c2, _, _ = PS2[i]
    x, c = X[i]
    PS1.append([c0 + c - x, i + 1, c0 + c])
    PS2.append([c0 + c - x * 2, i + 1, c0 + c])

for i in range(N):
    c1, xx, c0 = QS1[i]
    c2, _, _ = QS2[i]
    x, c = X[N - i - 1]
    x = C - x
    QS1.append([c0 + c - x, i + 1, c0 + c])
    QS2.append([c0 + c - x * 2, i + 1, c0 + c])

PS1.sort(reverse=True)
PS2.sort(reverse=True)

"""
print(PS1)
print(PS2)
print(QS1)
print(QS2)
"""

ans = 0
ps1index, ps2index = 0, 0
for q in range(N + 1):
    while PS1[ps1index][1] + q > N:
        ps1index += 1
    while PS2[ps2index][1] + q > N:
        ps2index += 1
    a1 = PS1[ps1index][0] + QS2[q][0]
    a2 = PS2[ps2index][0] + QS1[q][0]
    ans = max(ans, a1, a2)

print(ans)
