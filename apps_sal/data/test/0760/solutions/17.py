def match(str1, str2):
    for t in range(len(str1)):
        if str1[t]!=str2[t] and str2[t]!='_':
            return False
    return True

string=input()
k=int(input())

length=len(string)
mark = False
if k>=length:
    print(2*int((length+k)/2))
else:
    s=string+k*'_'
    n=int(len(s)/2)
    for i in range(n, 0, -1):
        for j in range(len(s)-2*i+1):
            if match(s[j:i+j], s[i+j:i+i+j]) and mark == False:
                print(2*i)
                mark = True
