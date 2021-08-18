N, A, B = list(map(int, input().split()))

if A * B < N or A + B - 1 > N:
    print((-1))
    return

rev = (B > A)
A, B = max(A, B), min(A, B)
B -= 1
M = N
ans1 = []
ans2 = []
while M > 0:
    if len(ans1) == len(ans2):
        temp = [i for i in range(M + 1 - A, M + 1)]
        ans1.append(temp)
        M = M - A
        A -= 1
    else:
        temp = [i for i in range(M + 1 - B, M + 1)]
        temp = temp[::-1]
        ans2.append(temp)
        M = M - B
        B -= 1

ans2 = ans2[::-1]
res = []
for L in ans1:
    res += L
for L in ans2:
    res += L

res = [val for val in res if val > 0]
if rev:
    res = res[::-1]
print((*res))
