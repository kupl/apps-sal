k = int(input())
n = [int(i) for i in input()]
s = sum(n)
n.sort()
i=0
while i<len(n) and s<k:
    s+=9-n[i]
    i+=1 
print(i)

