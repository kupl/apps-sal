P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
S = [0]*25

N = int(input())
for i in range(2, N+1):
    num = i
    j = 0
    while num > 1:
        if num%P[j] == 0:
            num //= P[j]
            S[j] += 1
        else:
            j += 1
            if j == 25:
                break

# 74
# 2 24
# 4 14
# 2 4 4

ans = 0
if S[0] >= 74:
    ans += 1
for i in range(3):
    if S[i] >= 24:
        tmp = -1
        for num in S:
            if num >= 2:
                tmp += 1
        ans += tmp
for i in range(4):
    if S[i] >= 14:
        tmp = -1
        for num in S:
            if num >= 4:
                tmp += 1
        ans += tmp
tmp4 = 0
tmp2 = 0
for num in S:
    if num >= 4:
        tmp4 += 1
    if num >= 2 and num < 4:
        tmp2 += 1
ans += tmp4*(tmp4-1)*(tmp4+tmp2-2)//2
print(ans)
