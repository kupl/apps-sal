from sys import stdin, stdout

k = int(stdin.readline().rstrip())
n = int(stdin.readline().rstrip())

nList = list(map(int,list(str(n))))

nList.sort()
currentSum = sum(nList)

i=0
while currentSum<k:
    currentSum+=(9-nList[i])
    i+=1

print(i)

