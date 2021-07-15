N = int(input())
S = [i for i in input()]
ANS = []

for i in range(1, N+1):
    ans = 0
    A = []
    B = []
    A = list(set(S[:i]))
    B = list(set(S[i:]))
    for a in A:
        for b in B:
            if a == b:
                ans += 1
    ANS.append(ans)
print(max(ANS))
