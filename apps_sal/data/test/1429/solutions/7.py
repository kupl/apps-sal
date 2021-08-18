N, S = input().split()
N = int(N)
left_AT_number = [0] * (N + 1)
left_CG_number = [0] * (N + 1)
AT = 0
CG = 0
for j in range(N):
    if S[j] == "A":
        AT += 1
    elif S[j] == "T":
        AT -= 1
    elif S[j] == "C":
        CG += 1
    else:
        CG -= 1
    left_AT_number[j + 1] = AT
    left_CG_number[j + 1] = CG
ans = 0
i_CG = 0
i_AT = 0
for i in range(N):
    i_CG = left_CG_number[i]
    i_AT = left_AT_number[i]
    for k in range(i + 1, N + 1):
        if i_CG - left_CG_number[k] == 0 and i_AT - left_AT_number[k] == 0:
            ans += 1
print(ans)
