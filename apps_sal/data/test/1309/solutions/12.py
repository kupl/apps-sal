n = int(input())
w = list(map(int,input().split()))
w.sort()
instability = list()
for i in range(2*n):
    for j in range(i+1, 2*n):
        cnt = 0
        for k in range(2*n):
            if k < i or k > j:
                if k % 2 == 0:
                    cnt -= w[k]
                else:
                    cnt += w[k]
            if k > i and k < j:
                if k % 2 == 0:
                    cnt += w[k]
                else:
                    cnt -= w[k]
        instability.append(cnt)
print(min(instability))
                
                
        

