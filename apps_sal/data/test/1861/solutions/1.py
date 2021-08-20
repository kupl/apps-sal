(n, k) = list(map(int, input().split()))
cards = set()
L = []
x = ord('S') + ord('E') + ord('T')
total = 0
for i in range(n):
    s = input()
    cards.add(s)
    L.append(s)
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        opposite = []
        for l in range(k):
            if L[i][l] == L[j][l]:
                opposite.append(L[i][l])
            else:
                opposite.append(chr(x - ord(L[i][l]) - ord(L[j][l])))
        if ''.join(opposite) in cards:
            total += 1
print(total // 6)
