S = ['0'] + list(input()) + ['0']
N = len(S)
flag = False

ans = 0

for i in range(N - 1, 0, -1):
    j = int(S[i])
    if flag:
        j += 1
        S[i] = j

    if j <= 5:
        if j == 5 and int(S[i - 1]) >= 5:
            ans += j
            flag = True
        else:
            ans += j
            flag = False

    else:
        ans += 10 - j
        flag = True

if flag:
    ans += 1


# print (ans)
count = 0
for s in S:
    if s == 5:
        count += 1
    else:
        ans -= max(0, count - 2)
        count = 0

print(ans)
