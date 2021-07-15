s = str(input().strip())
t = list(s[::-1])
cnt = 0
for i,v in enumerate(t):
    if v == '0':
       cnt += 1
    else:
        if cnt:
            cnt -= 1
        else:
            t[i] = '0'
print("".join(t[::-1]))
