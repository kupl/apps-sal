L = sorted(list(map(int, input().split())))
cnt = 0
while L[0] < L[2] - 2:
    cnt += 1
    L[0] += 2
while L[1] < L[2] - 2:
    cnt += 1
    L[1] += 2
if L[0] % 2 == L[1] % 2 and L[1] % 2 == L[2] % 2:
    if L[0] < L[2]:
        cnt += 1
    if L[1] < L[2]:
        cnt += 1
elif L[0] == L[1]:
    cnt += 1
elif L[1] == L[2]:
    cnt += 2
else:
    cnt += 3
print(cnt)
