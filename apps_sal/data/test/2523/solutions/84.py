S = input()
N = len(S)
center_i = N // 2
center = S[center_i]

ans = N // 2
l = r = center_i
if N % 2 == 0:
    l -= 1
while l >= 0:
    if not (S[l] == center == S[r]):
        break
    l -= 1
    r += 1
    ans += 1
print(ans)
