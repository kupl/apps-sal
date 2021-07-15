[N, X, M] = [int(i) for i in input().split()]
L = [X]
ans = X
dic = {}
for i in range(1, N):
    t = (L[-1]**2)%M
    if t in dic:
        x = dic[t]
        ans += (sum(L[x:i+1])) * ((N-i)//(i-x)) + sum(L[x:x+(N-i)%(i-x)])
        break
    else:
        L.append(t)
        dic[t] = i
        ans += t
 
print(ans)
