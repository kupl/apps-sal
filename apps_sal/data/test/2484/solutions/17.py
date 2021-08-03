nim = int(input())
mike = list(map(int, input().split()))

S = [0]
X = [0]
for a in mike:
    S.append(S[-1] + a)
    X.append(X[-1] ^ a)

l, r = 1, 1
result = 0
p = 1
while r <= nim:
    if S[r] - S[l - 1] == X[r] ^ X[l - 1]:
        if p == 0:
            result -= (r - l) * (r - l + 1) // 2
        r += 1
        p = 1
    else:
        if p == 1:
            result += (r - l) * (r - l + 1) // 2
        l += 1
        p = 0
result += (r - l) * (r - l + 1) // 2
print(result)
