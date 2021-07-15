a, b = map(int, input().split())
do = []
while True:
    do.append(b)
    if b == a:
        break
    if b % 2 == 0:
        b //= 2
    elif str(b)[-1] == '1':
        if b == 1:
            if a == 1:
                break
            else:
                print("NO")
                return                
        else:
            b = int(str(b)[:-1])
    else:
        print("NO")
        return
do = do[::-1]
print("YES")
print(len(do))
print(*do)
