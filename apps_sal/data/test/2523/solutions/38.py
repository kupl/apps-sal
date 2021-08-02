S = input()
N = len(S)

if len(set(S)) == 1:
    print(N)
    return

K = (N + 1) // 2
X = set()
if N & 1:
    X = {S[K - 1]}
    l = K - 2
    r = K
else:
    X = set()
    l = K - 1
    r = K

while l:
    X.add(S[l])
    X.add(S[r])
    if len(X) > 1:
        break
    K += 1
    l -= 1
    r += 1

print(K)
