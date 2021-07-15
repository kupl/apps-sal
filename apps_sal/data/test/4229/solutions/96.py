n = int(input())
l = []
for i in range(1,n+1) :
    if i%3 != 0 and i%5 != 0 :
        l.append(i)
print(sum(l))
