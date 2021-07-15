n,m = map(int,input().split())
a = [[],[],[]]
for _ in range(n):
    x,y = map(int,input().split())
    a[x-1].append(y)

for i in range(3):
    a[i].sort(reverse=True)

a_one_odd = []
a_one_even = []
a_length = [len(a[i]) for i in range(3)]
for i in range(0,a_length[0]-1,2):
    a_one_even.append(a[0][i]+a[0][i+1])
for i in range(1,a_length[0]-1,2):
    a_one_odd.append(a[0][i]+a[0][i+1])
data_even = sorted(a_one_even+a[1],reverse=True)
data_odd = sorted(a_one_odd+a[1],reverse=True)

data_sum_even = [0]
for x in data_even:
    data_sum_even.append(data_sum_even[-1]+x)
data_sum_odd = [0]
for x in data_odd:
    data_sum_odd.append(data_sum_odd[-1]+x)

data_sum_three = [0]
for x in a[2]:
    data_sum_three.append(data_sum_three[-1]+x)

ans = 0
#print(data_sum_odd,data_sum_even,data_sum_three)
for k in range(a_length[2]+1):
    if m-3*k < 0:break
    now1,now2 = data_sum_three[k],data_sum_three[k]
    if (m-3*k)%2== 0:
        now1 += data_sum_even[min((m-3*k)//2,len(data_sum_even)-1)]
        if a_length[0] > 0 and m-3*k > 0:
            now2 += a[0][0]
        if (m-3*k)//2 >= 1:
            now2 += data_sum_odd[min((m-3*k)//2-1,len(data_sum_odd)-1)]
    else:
        now1 += data_sum_even[min((m-3*k)//2,len(data_sum_even)-1)]
        if a_length[0] > 0 and m-3*k > 0:
            now2 += a[0][0]
        now2 += data_sum_odd[min((m-3*k-1)//2,len(data_sum_odd)-1)]
    ans = max(ans,now1,now2)


print(ans)
