# これほんと納得行かない
N, P = list(map(int, input().split()))
S = list(map(int, input()))
if P==2 or P==5:
    ans = 0
    for i, c in enumerate(S, 1):
        if c%P==0:
            ans += i
    print(ans)
    return
L = [0] * P
cum = 0
ans = 0
L[0] += 1
inv10 = pow(10, P-2, P)
base = 1
for c in S:
    cum = (cum + c * base) % P
    base = base * inv10 % P
    ans += L[cum]
    L[cum] += 1
print(ans)

