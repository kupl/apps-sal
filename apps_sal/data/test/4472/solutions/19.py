n = int(input())
a = input()
b = input()
p = 0
for i in range(n//2):
    if((a[i] != b[i]) and (a[i] != b[n-i-1]) and (a[i] != a[n-i-1])):
        p+=1
        if((b[i] != b[n-i-1]) and (a[n-1-i] != b[i]) and (a[n-1-i] != b[n-i-1]) and (a[n-1-i] != a[i])):
            p+=1
    else:
        if(a[i] == b[i]):
            if(a[n-i-1] != b[n-i-1]):
                p+=1
        elif(a[i] == b[n-i-1]):
            if(a[n-i-1] != b[i]):
                p+=1
        else:
            if(b[n-i-1] != b[i]):
                p+=2
if((a[n//2] != b[n//2]) and (n%2==1)):
    p+=1
print(p)

