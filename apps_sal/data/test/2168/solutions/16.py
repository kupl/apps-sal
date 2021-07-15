n = int(input())

c = []
w = 0
while w<n:
    c.append(list(map(int, input().split())))
    m = c[w][0]
    c[w]=[max(c[w][1:m+1]), m]
    w+=1

w=0
prise = c[w][0]
count = c[w][1]
sum =0
while w<n-1:
    w += 1
    f = c[w][0]
    l = c[w][1]
    if f>=prise:
        sum+= count*(f-prise)
        prise = f
    else:
        sum += l * (prise - f)
    count += l
print(sum)
