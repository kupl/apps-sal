A,B = list(map(int,input().split()))
xor = []
if B-A<=8:
    ans = 0
    for i in range(A,B+1):
        ans^=i
else:
    while True:
        if A%4 == 0:
            break
        else:
            xor.append(A)
        A+=1

    while True:
        if B%4 == 3:
            break
        else:
            xor.append(B)
        B-=1

    ans = 0
    while xor:
        ans^=xor.pop()
print(ans)

