N = int(input())
CSF = [list(map(int, input().split())) for i in range(N - 1)]
ans = []
for i in range(N - 1):
    temp = 0
    for j in range(i, N - 1):
        (c, s, f) = (CSF[j][0], CSF[j][1], CSF[j][2])
        if temp <= s:
            temp += s - temp
            temp += temp % f
        else:
            temp += (f - (temp - s) % f) % f
        temp += c
    ans.append(temp)
for i in range(N - 1):
    print(ans[i])
print(0)
