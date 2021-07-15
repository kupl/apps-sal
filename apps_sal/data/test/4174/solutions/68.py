N,X = map(int,input().split())
L_List = list(map(int,input().split()))
ans = 0
ct = 1
for i in range(N):
    ans += L_List[i]
    if ans <= X:
        ct += 1
    else:
        break
        
print(ct)
