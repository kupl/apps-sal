l,r = list(map(int, input().split()))
ans = 0
for i in range(40):
    for j in range(40):
        v= int(2**i * 3**j);
        if(v >= l and v <= r):
            ans = ans + 1
    
print(ans)

