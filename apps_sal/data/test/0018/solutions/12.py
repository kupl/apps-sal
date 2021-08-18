s = input()
iterate = 0
e = [(True) for i in range(len(s))]
ans = ['' for i in range(len(s))]
idx = 0

lastOccur = [-1 for i in range(26)]

for i in range(len(s)):
    lastOccur[ord(s[i]) - ord('a')] = i

i = 0
while(i < 26 and iterate < len(s)):
    j = iterate - 1
    while(j >= 0 and ord(s[j]) - ord('a') <= i):
        if(e[j]):
            ans[idx] = s[j]
            e[j] = False
            idx += 1
        j -= 1

    j = iterate
    while(j < lastOccur[i] + 1):
        if(e[j] and ord(s[j]) - ord('a') == i):
            ans[idx] = s[j]
            e[j] = False
            idx += 1
        j += 1
    iterate = j
    i += 1

if(iterate >= len(s)):
    for j in range(len(s) - 1, -1, -1):
        if(e[j]):
            ans[idx] = s[j]
            idx += 1


str1 = ''.join(ans)
print(str1)
