a,b,c = map(int, input().split())

flag = True

for i in range(b):
    if (a*(i+1))%b == c:
        print("YES")
        flag = False
        break
    
if flag:
    print("NO")
