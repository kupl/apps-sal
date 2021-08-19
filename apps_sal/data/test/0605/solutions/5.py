(pM, pV, tM, tV) = list(map(int, input().split()))
misha = max(3 * pM // 10, pM - pM // 250 * tM)
vasya = max(3 * pV // 10, pV - pV // 250 * tV)
if misha == vasya:
    print('Tie')
elif misha > vasya:
    print('Misha')
else:
    print('Vasya')
