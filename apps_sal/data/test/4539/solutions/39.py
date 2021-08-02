N = int(input())
S = str(N)
L = len(S)
total = 0
for i in range(L):
    total += int(S[i])
if N % total == 0:
    ans = "Yes"
else:
    ans = "No"
print(ans)
