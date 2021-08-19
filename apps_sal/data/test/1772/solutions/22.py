n = u = o = 0
cnt = 0
n = int(input())
i = 0
x = input()
x = x + '                     '
while cnt < n:
    if x[i] is ' ':
        i += 1
        continue
    else:
        a = int(x[i])
        if x[i + 1] is ' ':
            if a % 2 == 0:
                u += 1
            else:
                o += 1
            cnt += 1
    i += 1
ans = min(u, o)
u -= ans
o -= ans
ans += int(o / 3)
print(ans)
