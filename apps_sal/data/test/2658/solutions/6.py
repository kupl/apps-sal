N,K=map(int,input().split())
A = list(map(int,input().split()))
count = 0
now = 1
city = [1]
city2 = {1}
while count < K:
    count +=  1
    now = A[now-1]
    if now in city2:
        break
    else:
        city.append(now)
        city2.add(now)
if count == K:
    print(now)
else:
    n = city.index(now)
    K -= n
    count -= n
    K %= count
    print(city[n+K])
