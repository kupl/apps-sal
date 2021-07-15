N,M = map(int,input().split())
S = list(input())
#print(S)
S.reverse()

if S[0] == 1 or S[-1] == 1:
    det = -1
else:
    det = 0
    count = 0
    data = []
    for i in range(N+1):
        if S[i] == "0":
            data.append(count+1)
            count = 0
        else:
            count += 1
        if count == M:
            det = -1
            break
    #print(data)
    
if det != -1:
    ans = []
    count = 0
    for i in range(1,len(data)):
        if count + data[i] > M:
            ans.append(count)
            count = data[i]
        else:
            count += data[i]
    ans.append(count)
    ans.reverse()
    print(" ".join(map(str,ans)))

else:
    print(-1)
