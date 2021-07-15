s = input()
cnt = [0] * 256
for i in s:
    cnt[ord(i)] += 1
i = ord('a')
j = ord('z')
while i < j:
    while i < j and cnt[i] % 2 == 0:
        i += 1
    while i < j and cnt[j] % 2 == 0:
        j -= 1
    if i < j:
        cnt[i] += 1
        cnt[j] -= 1
        i += 1
        j -= 1
res1 = ''
res2 = ''
c = ''
for i in range(ord('a'), ord('z') + 1):
    res1 = res1 + chr(i) * (cnt[i] // 2)
    res2 = chr(i) * (cnt[i] // 2) + res2
    if cnt[i] % 2 == 1:
        c = chr(i)
print(res1 + c + res2)
