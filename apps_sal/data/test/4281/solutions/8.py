
n = int(input())

x = list(map(int,input().split()))

x.sort()


y = [] #to min

for i in range(n):
    if i == 0 or x[i-1] != x[i]:
        y.append(x[i])

yend = [True] * len(y)
ansmin = len(y)

for i in range(len(y)):

    if i == 0 or ( not yend[i] ):
        continue

    if y[i-1] + 1 == y[i] and yend[i-1]:
        yend[i-1] = False
        ansmin -= 1
        yend[i] = False

        if i+1 < len(y) and y[i+1] - 1 == y[i]:
            yend[i+1] = False
            ansmin -= 1

    elif y[i-1] + 2 == y[i] and yend[i-1]:
        yend[i-1] = False
        yend[i] = False
        ansmin -= 1
 
#print (yend)


dic = {}

for i in range(n):

    if x[i] - 1 not in dic:
        dic[x[i] - 1] = 1
    elif x[i] not in dic:
        dic[x[i]] = 1
    else:
        dic[x[i] + 1] = 1

print (ansmin , len(dic))
