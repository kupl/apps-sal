import sys

N, P = list(map(int, input().split()))
A = input()

ans = 0

if 10 % P == 0:
    for r in range(len(A)):
        if int(A[r]) % P == 0:
            ans += r + 1
    print(ans)
    return


A = "0" + A[::-1]

S = [0] * len(A)
cnt = [0] * P
cnt[0] = 1

for i in range(len(A) - 1):
    S[i + 1] = (S[i] + int(A[i + 1]) * pow(10, i, P)) % P
    cnt[S[i + 1] % P] += 1
# print(S, cnt)

# ans = cnt[0] * (cnt[0] - 1) // 2
for c in cnt:
    ans += c * (c - 1) // 2
print(ans)

