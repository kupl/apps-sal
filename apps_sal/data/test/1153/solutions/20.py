# cook your dish here
s=input().split(" ")
a=int(s[0])
b=int(s[1])

s=input().split(" ")
arr1=[int(i) for i in s]
s=input().split(" ")
arr2=[int(i) for i in s]

i=0
j=0
sum1=arr1[0]
sum2=arr2[0]

files=0

while True:
    
    if sum1==sum2:
        i+=1
        j+=1
        files+=1
        if i>=a or j>=b:
            break;
        sum1=arr1[i]
        sum2=arr2[j]
    if sum1<sum2:
        i+=1 
        if i>=a or j>=b:
            break;
        sum1+=arr1[i]
    if sum1>sum2:
        j+=1 
        if i>=a or j>=b:
            break;
        sum2+=arr2[j]
        
print (files)

