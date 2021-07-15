import sys
from collections import Counter
N = int(input())
S = list(input())
Sc = Counter(S)
R = Sc["R"]
G = Sc["G"]
B = Sc["B"]
if R == 0 or G == 0 or B == 0:
    print((0))
    return
else:
    ans = R*G*B
for i in range(1, N//2+2):
    for j in range(N):
        if j+i+i >= N:
            break
        if S[j] == S[j+i]:
            continue
        if S[j] == S[j+i+i]:
            continue
        if S[j+i] == S[j+i+i]:
            continue
        ans -= 1
print(ans)

