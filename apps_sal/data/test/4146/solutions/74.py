from collections import Counter

n = int(input())
A = list(map(int, input().split()))

kisu = A[0::2]
gusu = A[1::2]

CK = Counter(kisu)
CG = Counter(gusu)
CKM = CK.most_common(2)
CGM = CG.most_common(2)

if len(CKM) == 1 and len(CGM) == 1:
    if CKM[0][0] == CGM[0][0]:
        ans = n // 2
    else:
        ans = 0
elif len(CKM) == 1:
    if CKM[0][0] == CGM[0][0]:
        ans = n // 2 - CGM[1][1]
    else:
        ans = n // 2 - CGM[0][1]
elif len(CGM) == 1:
    if CKM[0][0] == CGM[0][0]:
        ans = n // 2 - CKM[1][1]
    else:
        ans = n // 2 - CKM[0][1]
else:
    if CKM[0][0] == CGM[0][0]:
        ans1 = n // 2 - CKM[1][1] + n // 2 - CGM[0][1]
        ans2 = n // 2 - CGM[1][1] + n // 2 - CKM[0][1]
        ans = min(ans1, ans2)
    else:
        ans = n - (CKM[0][1] + CGM[0][1])

print(ans)
