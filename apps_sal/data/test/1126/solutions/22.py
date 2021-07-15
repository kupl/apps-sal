n, x, m = list(map(int, input().split()))

visit = [-1] * m
a_sum = [0] *(m+1)

a = x
a_sum[1] = x
visit[a] +=1

flg = True

if n == 1:
    print(x)
    return
if x == 0:
    print((0))
    return

for i in range(1,n):
    a = (a**2)%m
    a_sum[i+1] = a_sum[i] + a
    if visit[a] == -1:
        visit[a] = i
    else:
        li = visit[a] 
        roop = i - li
        roop_sum = a_sum[i]-a_sum[li]
        flg = False
        break

if flg:
    print((a_sum[i+1]))
    return

sum = a_sum[li] 
sum += roop_sum*((n-li)//roop)
sum += a_sum[li + (n-li)%roop] - a_sum[li]

print(sum)






