A,B,C,D = map(int,input().split())

taka = 0
aoki = 0

while A > 0:
    A -= D
    taka += 1
    
while C > 0:
    C -= B
    aoki += 1
    
if taka >= aoki:
    print("Yes")
else:
    print("No")
