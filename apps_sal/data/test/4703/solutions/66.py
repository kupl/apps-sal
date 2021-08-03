S = input()
ans = 0
for i in range(2**(len(S) - 1)):
    tmp = int(S[0])
    for j in range(1, len(S)):
        if i & 1 == 1:
            ans += tmp
            tmp = int(S[j])
        else:
            tmp = tmp * 10 + int(S[j])
        i = i >> 1
    ans += tmp
print(ans)
