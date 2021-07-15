a = int(input())
s = input()

sm ={}
for i in range(len(s)):
    for j in range(i,len(s)):
        if j== i:
            t = int(s[j])
        else:
            t += int(s[j])
        if t in sm:
            sm[t] += 1
        else:
            sm[t] = 1
if a==0:
    if 0 in sm:
        sum_pairs = (len(s)*(len(s)+1))//2
        print((sm[0]*(sum_pairs))+(sm[0]*((sum_pairs) - sm[0])))
    else:
        print(0)
else:
    c = 0
    for f in sm:
        if f != 0  and a % f == 0 and (a//f) in sm:
            c += sm[f] * sm[a//f]

    print(c)


