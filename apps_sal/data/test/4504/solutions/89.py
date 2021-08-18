S = input()
lenS = len(S)
if lenS % 2 == 0:
    S = S[:-1]

ans = 0
for i in range(1, lenS, 2):
    idx = -i
    _S = S[:idx]
    idx = len(_S) // 2
    if _S[:idx] == _S[idx:]:
        ans = len(_S)
        break
print(ans)
