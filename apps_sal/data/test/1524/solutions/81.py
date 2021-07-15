s = str(input())
n = len(s)
RL = [0] * n
ans = [0] * n
for i in range(n-1):
    if s[i] == 'R' and s[i+1] == 'L':
        RL[i] = 1
        RL[i+1] = -1
for i in range(n):
    if RL[i] == 1:
        cnt = 1
        i_temp = i
        while i_temp > 0 and s[i_temp-1] == 'R':
            i_temp -= 1
            cnt += 1
        ans[i] += (cnt + 1) // 2
        ans[i+1] += cnt // 2
    if RL[i] == -1:
        cnt = 1
        i_temp = i
        while i_temp + 1 < n and s[i_temp+1] == 'L':
            i_temp += 1
            cnt += 1
        ans[i] += (cnt + 1) // 2
        ans[i-1] += cnt // 2
for i in range(n-1):
    print(ans[i], end=" ")
print(ans[n-1])
