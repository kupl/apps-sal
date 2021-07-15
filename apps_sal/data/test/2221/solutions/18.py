x1, y1 = [int(x) for x in input().split()]
x2, y2 = [int(x) for x in input().split()]
lens=int(input())
string=input()
x = [0 for _ in range(lens + 1)]
y = [0 for _ in range(lens + 1)]
for i in range(lens):
    x[i + 1] = x[i] + (string[i] == "R") - (string[i] == "L")
    y[i + 1] = y[i] + (string[i] == "U") - (string[i] == "D")
    

left = -1
rite = int(10 ** 18)
ans = int(10 ** 18) + 1
while rite - left > 1:
    mid = (left + rite) >> 1
    X = (mid // lens) * x[-1] + x[mid % lens]
    Y = y[-1] * (mid // lens) + y[mid % lens]
    X += x1
    Y += y1
    if abs(X - x2) + abs(Y - y2) <= mid: rite = mid
    else: left = mid
        
print([rite, -1][rite == 10 ** 18])        
    
     
    


