s = input()
s_sum = []
for i in range(2**(len(s)-1)):
    sj = 0
    a = 0
    for j in range(len(s)-1):
        if ((i>>j) & 1):
            a += int(s[sj:j+1])
            sj = j+1
    a += int(s[sj:])
    s_sum.append(a)
print(sum(s_sum))  
