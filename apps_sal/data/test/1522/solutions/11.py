n = int(input())
s = input()
er = {}
ers = set()
cnt = 0
for i in range(len(s)):
    if i % 2 == 0:
        if ord(s[i]) in ers:
            er[ord(s[i])] += 1
        else:
            ers.add(ord(s[i]))
            er[ord(s[i])] = 1
    else:
        if ord(s[i]) + 32 in ers and er[ord(s[i]) + 32] >= 1:
            er[ord(s[i]) + 32] -=  1
        else:
            cnt += 1
print(cnt)
        
        

