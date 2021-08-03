k, n = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = [0] * k
for i in range(k):
    if i == 0:
        S[0] = A[0]
    else:
        S[i] = S[i - 1] + A[i]
S.sort()
B.sort()
ans = set()
for i, s in enumerate(S):
    if i > 0 and S[i - 1] == s:
        continue
    t = B[0] - s
    if n > 1:
        j = i + 1
        flag = False
        for m, u in enumerate(B[1:]):
            while j < len(S):
                if u - S[j] == t:
                    if m == n - 2:
                        flag = True
                    j += 1
                    break
                else:
                    j += 1
        if flag == True:
            ans.add(t)
    else:
        ans.add(t)
print(len(ans))
