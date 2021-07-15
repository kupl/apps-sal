m,n,k,t = list(map(int,input().split()))
a = [0] + sorted(list(map(int,input().split()))) + [3*10**5]
data = sorted([list(map(int,input().split())) for _ in range(k)])
#print(data)

ok = m+1
ng = 0

while ok-ng > 1:
    mid = (ok + ng)//2
    A = a[mid]

    interval_set = []
    for i in range(k):
        if data[i][2]<= A:
            continue
        if len(interval_set)==0:
            interval_set.append([data[i][0],data[i][1]])
        else:
            if interval_set[-1][1] < data[i][0]:
                interval_set.append([data[i][0],data[i][1]])
            elif interval_set[-1][1] < data[i][1]:
                new_interval = [interval_set.pop()[0],data[i][1]]
                interval_set.append(new_interval)
    time = n+1
    for interval in interval_set:
        time += (interval[1]-interval[0]+1)*2

    #print(mid,A, interval_set,time)
    if time <= t:
        ok = mid
    else:
        ng = mid

print(m-ok+1)
#print(a[ok])

