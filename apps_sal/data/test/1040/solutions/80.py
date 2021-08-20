n = int(input())
s = input() + 'zzz'
t = 'zzz'
ans = n
cnt = 0
for i in range(n):
    if cnt >= n + 1:
        break
    if s[cnt:cnt + 3] == 'fox':
        ans -= 3
        cnt += 3
    else:
        t += s[cnt]
        cnt += 1
        if t[-3:] == 'fox':
            ans -= 3
            t = t[:-3]
print(ans)
