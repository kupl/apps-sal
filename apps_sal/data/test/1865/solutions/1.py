

n = int(input())
a = [int(s) for s in input().split()]

b = sorted(a)

count = 0
swaps = []
for i in range(n):
    if a[i]!=b[i]:
        count += 1
        for j in range(i,n):
            if a[j]==b[i]:
                a[i],a[j]=a[j],a[i]
                swaps.append((i,j))
                break

print(count)
for i,j in swaps:
    print(i,j)
        
        
##while 1>0:
##    line = input()
##    if len(line.split())==0:
##        break
##    print(line)

