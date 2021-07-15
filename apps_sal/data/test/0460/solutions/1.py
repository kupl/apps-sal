from sys import stdin, stdout

def findWinners(s):
    winSet=set()
    i=(s//50)%475
    for _ in range(25):
        i = (i*96+42)%475
        winSet.add(26+i)
    return winSet


p,x,y = list(map(int, stdin.readline().rstrip().split()))

x1=x
successfulHacks=0
winning=False
while x1>=y and not winning:
    if p in findWinners(x1):
        winning=True
    x1-=50
    
while not winning:
    x+=100
    successfulHacks+=1
    if p in findWinners(x) or p in findWinners(x-50):
        winning=True

print(successfulHacks)

