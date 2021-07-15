s,value = map(int,input().split())
li = []
for j in range(s):
    li.append(j+1)

for i in range(value):
    n = int(input())
    li_s = list(map(int,input().split()))
    for k in range(n):
        if li_s[k] in li:
            li.remove(li_s[k])
            
print(len(li))
