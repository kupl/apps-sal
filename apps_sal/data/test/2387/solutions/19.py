N = int(input())
G2, G4 = [], []
cnt2 = 0
cnt3 = 0
for _ in range(N):
    S = input()
    MIN = 0
    cnt = 0
    for s in list(S):
        if s == '(':
            cnt += 1
        else:
            cnt -= 1
        MIN = min(MIN, cnt)
    if MIN == 0 and cnt >= 0:
        cnt2 += cnt
    if MIN < 0 and cnt >= 0:
        G2.append([MIN, cnt])
    if MIN == cnt and cnt < 0:
        cnt3 += cnt
    if MIN < cnt and cnt < 0:
        G4.append([MIN, cnt])


G2.sort(reverse=True)
for L in G2:
    if cnt2 + L[0] < 0:
        print('No')
        return
    else:
        cnt2 += L[1]
for L in G4:
    if cnt2 + L[0] < 0:
        print('No')
        return
    else:
        cnt2 += L[1]

cnt2 += cnt3

if cnt2 == 0:
    print('Yes')
else:
    print('No')
