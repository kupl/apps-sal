n = int(input())
s = input()
d = []
pre = 0
for i in range(len(s)):
    if s[i] == '-':
        d.append(pre + 1)
        pre = 0
    elif s[i] == ' ':
        d.append(pre + 1)
        pre = 0
    else:
        pre += 1
d.append(pre)


def calc(k, n):
    m = len(d)
    tmp = 0
    cnt = 1
    for i in range(m):
        if d[i] > k:
            return False
        if tmp + d[i] <= k:
            tmp += d[i]
        else:
            tmp = d[i]
            cnt += 1

    return cnt <= n


l, r = 0, 10 ** 6 + 1
while r - l > 1:
    mid = (r + l) // 2
    if calc(mid, n):
        r = mid
    else:
        l = mid

print(r)
