A,B = list(map(int,input().split()))

answer = 0
X = A - 1
Y = B
answer = 0
for i in range(1,41):
    cycle = 2 ** i
    qX = X // cycle
    qY = Y // cycle
    rX = X % cycle
    rY = Y % cycle
    oneX = qX * cycle // 2
    oneY = qY * cycle // 2
    if rX >= cycle // 2:
        oneX += rX - cycle // 2 + 1
    if rY >= cycle // 2:
        oneY += rY - cycle // 2 + 1
    one = oneY - oneX

    if one % 2 == 1 :
        answer += 2 ** (i - 1)
    
print(answer)
