s = input()
lst=[0]
for i in range(1,len(s)+1):
    lst.append(lst[-1]+1/i)
x=lst[len(s)]
res=0
for i,j in enumerate(s):
    if j in 'AEIOUY':
        res+=x
    x+=lst[len(s)-i-1]-lst[i+1]
print(res)
