
N = int(input())
count = [0] * 5
for i in range(N):
    tmp = input()
    if tmp[0] == "M":
        count[0] += 1
    if tmp[0] == "A":
        count[1] += 1
    if tmp[0] == "R":
        count[2] += 1
    if tmp[0] == "C":
        count[3] += 1
    if tmp[0] == "H":
        count[4] += 1

ans = 0
for i in range(0, 3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            ans += count[i] * count[j] * count[k]

print(ans)
