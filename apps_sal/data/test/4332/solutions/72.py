N = int(input())
S = str(N)
n = 0
for i in range(len(S)):
    n += int(S[i])
if N % n == 0:
    print("Yes")
else:
    print("No")
