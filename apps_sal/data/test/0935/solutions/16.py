n, m = tuple(map(int, input().split(' ')))
move = 1
# 1 - AKHSHAT
while(True):
    n -= 1
    m -= 1
    if (n<1 or m<1):
        break
    move += 1
        
if move%2==1:
    print("Akshat")
else:
    print("Malvika")
