n = int(input())
s = input()

prr = []
while len(s) > 0:
    k = 0
    for i in range(len(s) - 1, -1, -1):
        if(s[i] == '0'):
            continue
        if(int(s[i:]) >= n or len(s[i:]) > len(str(n))):
            k = i + 1
            while(k < len(s) and s[k] == '0'):
                k += 1
            if(k == len(s)):
                k = len(s) - 1
            break
    prr.append(int(s[k:]))
    s = s[:k]
sum = 0
for i in range(len(prr) - 1, -1, -1):
    sum *= n
    sum += prr[i]

print(sum)
