n = int(input())
vessel = [int(i) for i in input().split()]
water_amount = [0] * n
m = int(input())
next_vessel = [int(i) for i in range(1,n + 1)]
answer = []

for i in range(m):
    query = [int(j) for j in input().split()]
    
    if query[0] == 1:
        k = query[1] - 1
        skip_vessel = []
        while k < n:
            delta = vessel[k] - water_amount[k]
            if delta <= query[2]:
                water_amount[k] = vessel[k]
                query[2] -= delta
                skip_vessel.append(k)
                k = next_vessel[k]
            else:
                water_amount[k] += query[2]
                break
        for j in skip_vessel:
            next_vessel[j] = k
            
    else:
        answer.append(water_amount[query[1] - 1])

print(*answer, sep = '\n')

