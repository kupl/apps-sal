(n, m) = map(int, input().split())
otr = []
for i in range(n):
    otr.append([int(j) for j in input().split()])
answer = 0
s = []
for i in range(1, m + 1):
    Ok = True
    for j in range(n):
        if otr[j][0] <= i and otr[j][1] >= i:
            Ok = False
    if Ok:
        s.append(i)
        answer += 1
print(answer)
print(' '.join(map(str, s)))
