n, k = map(int, input().split())
M = list(map(int, input().split()))
for i in range(n):
    M[i] = (M[i], i + 1)
M.sort()
if M[0][0] > k:
    print(0)
else:
    used = 0
    i = 0
    Ans = []
    while i < n and used + M[i][0] <= k:
        Ans.append(M[i][1])        
        used += M[i][0]
        i += 1
    print(len(Ans))
    print(" ".join(map(str, Ans)))
