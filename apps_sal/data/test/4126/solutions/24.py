S = input()
l = len(S) // 2
former = S[:l]
latter = S[l + 1:]
print("Yes" if S == S[::-1] and former == former[::-1] and latter == latter[::-1] else "No")
