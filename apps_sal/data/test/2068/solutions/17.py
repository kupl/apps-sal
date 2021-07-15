def nafig(s):
    for i in range(len(s)):
        x = ord(s[i])
        if (x <= 90) and (x >= 65):
            x += 32
            s = s[:i] + chr(x) + s[i + 1:]
    return s


n = int(input())
dic = dict()
dic['polycarp'] = 1
maxim = 1
for i in range(n):
    st = list(map(str, input().split()))
    st[0] = nafig(st[0])
    st[2] = nafig(st[2])
    dic[st[0]] = dic[st[2]] + 1
    if dic[st[0]] > maxim:
        maxim = dic[st[0]]
print(maxim)



