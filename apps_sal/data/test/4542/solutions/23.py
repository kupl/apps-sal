S = input()
l = len(S)
ans = sum(a != b for a, b in zip(S[:l - 1], S[1:]))
print(ans)
