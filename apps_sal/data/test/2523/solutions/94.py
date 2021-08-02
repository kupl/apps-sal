S = input()

l = (len(S) - 1) // 2
r = len(S) // 2
m = S[l]
while l >= 0:
    if S[l] != m or S[r] != m:
        break
    l -= 1
    r += 1
if l < 0:
    print((len(S)))
else:
    print(r)
