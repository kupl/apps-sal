__author__ = 'sm'
#import sys
#fin = open('data.in','r')
#fout = open("data.out",'w')
#sys.stdin = fi:w
# n
#sys.stdout = fout

def readln():
    return list(map(int,input().split()))


n,d = readln()
data =  readln()
m = readln()[0]


data.sort()
cost = 0
j = 0
for i in range(m):
    if i >=  len(data):
        cost -= d
    else:
        cost += data[i]

print (cost)




