N, K, C = list(map(int, input().split()))
S = input()
A = []
cnt = 0
for i, s in enumerate(S, 1):
    if cnt > 0:
        cnt -= 1
    elif s == "o":
        cnt = C
        A.append(i)
if len(A) > K:
    return
B = []
cnt = 0
for i, s in zip(list(range(N, 0, -1)), S[::-1]):
    if cnt > 0:
        cnt -= 1
    elif s == "o":
        cnt = C
        B.append(i)
assert len(B) == K
B.reverse()
Ans = []
for a, b in zip(A, B):
    if a == b:
        Ans.append(a)
print(("\n".join(map(str, Ans))))

