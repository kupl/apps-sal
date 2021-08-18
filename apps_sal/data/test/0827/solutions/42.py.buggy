N = int(input())
T = input()

if T == '1':
    print((10**10 * 2))
    return
elif T == '0' or T == '10' or T == '11':
    print((10**10))
    return
elif T == '01':
    print((10**10 - 1))
    return
elif T == '00':
    print((0))
    return


left = T[:3]
if left == '110':
    l = 0
else:
    l = 1

right = T[-3:]
if right == '110':
    r = 0
else:
    r = 1

f = '110'
cnt = 0
i = 0
while True:
    if i + 3 > N:
        break
    s = T[i:i + 3]
    if s == f:
        cnt += 1
        i += 3
    elif int(s[0]) + int(s[1]) + int(s[2]) != 2:
        print((0))
        return
    else:
        i += 1

ans = 10**10 - (cnt - 1) - l - r
print(ans)
