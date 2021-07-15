K = int(input())

if K == 1:
    print(3)
    print(1,0,3)
elif K == 0:
    print(4)
    print(3,3,3,3)

else:
    div = -1
    
    if K <= 50:
        print(K)
        print(*[K for _ in range(K)])
    
    else:
        print(50)
        ans = [K//50+i for i in range(50)]

        for i in range(K%50):
            ans[i] += 50
            for j in range(50):
                if i != j:
                    ans[j] -= 1
        
        print(*ans)
