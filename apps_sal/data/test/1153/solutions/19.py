m,n=list(map(int,input().split(' ')))
a=list(map(int,input().split(' ')))
b=list(map(int,input().split(' ')))

count=0
s_a=a[0]
s_b=b[0]
i=0
j=0

while (i<m and j<n):
    if s_a==s_b:
        count+=1
        # print(s_a,s_b)
        i+=1
        j+=1
        if i<m and j<n:
            s_a=a[i]
            s_b=b[j]
    else:
        while(s_a!=s_b):
            while s_a<s_b:
                i+=1
                s_a+=a[i]
            while s_b<s_a:
                j+=1
                s_b+=b[j]
print(count)

