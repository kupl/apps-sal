n,m = list(map(int, input().split(' ')))
x = n//2 + (n%2==1)
y = n
for i in range(x, y+1) :
    if i%m == 0 :
        print(i)
        break
else :
    print(-1)

