N = int(input())
ls1 = []
for i in range(N):
    A = int(input())
    ls2 = []
    for i in range(A):
        x, y = map(int,input().split())
        ls2.append([x,y])
    ls1.append(ls2)
ans = 0
f = True
for i in range(2**N):
    for j in range(N):
        if (i>>j&1):
            f = True
            for k in ls1[j]:
                if (i >>(k[0] - 1) &1) == (k[1]&1):
                    continue
                else:
                    f = False
                    break
            if f == False:
                break
    if f:
        ans = max(ans,bin(i).count('1'))    
print(ans)
