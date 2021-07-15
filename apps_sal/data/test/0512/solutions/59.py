N = int(input())
el = []
for i in range(N):
    a,b = map(int,input().split())
    if a > 0 and b > 0 and a >= b:
        print("No")
        return
    el.append((a,b))
#print(el)
floor = [0]*2*N
for i in range(N):
    if el[i][0] != -1:
        if floor[el[i][0]-1] != 0:
            print("No")
            return
        floor[el[i][0]-1] = -(i+1)
    if el[i][1] != -1:
        if floor[el[i][1]-1] != 0:
            print("No")
            return
        floor[el[i][1]-1] = i+1
#print(floor)

dp = [False]*(N+1)
dp[0] = True
for i in range(1,N+1):
    for j in range(i+1):

        if dp[j] == True:
            
            l,r = j*2,i*2
            high = (r-l)//2
            for k in range(l,l+high):

                if floor[k] > 0:
                    break

                if floor[k+high] < 0:
                    break
                
                if floor[k] < 0:
                    if floor[k+high] != -floor[k] and floor[k+high] != 0:
                        break
                    elif floor[k+high] == 0:
                        if el[-floor[k]-1][1] != -1:
                            break
                            
                if floor[k+high] > 0:
                    if floor[k] != -floor[k+high] and floor[k] != 0:
                        break
                    elif floor[k] == 0:
                        if el[floor[k+high]-1][0] != -1:
                            break
            
            else:
                dp[i] = True
                break

def yn(p):
    if p:
        return "Yes"
    else:
        return "No"
print(yn(dp[-1]))
