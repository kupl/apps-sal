a=input()
b=input()
c = len(a)-len(b)
d=[]
for i in range(len(a)-len(b)+1):
    a[i:i+len(b)]
    count = 0
    for j in range(len(b)):
        if a[i:i+len(b)][j] == b[j]:
              count +=1
    d.append(len(b)-count)
print(min(d))    
