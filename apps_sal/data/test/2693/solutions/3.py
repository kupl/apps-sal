import math


def part(n, k):
    def _part(n, k, pre):
        if n <= 0:
            return []
        if k == 1:
            if n <= pre:
                return [[n]]
            return []
        ret = []
        for i in range(min(pre, n), 0, -1):
            ret += [[i] + sub for sub in _part(n - i, k - 1, i)]
        return ret
    return _part(n, k, n)


S, P, k = map(int, input().split())
factors = []

for i in range(1, int(math.sqrt(P)) + 1):
    if(P % i == 0 and P // i != i):
        factors.append(i)
        factors.append(P // i)
    elif(P % i == 0 and P // i == i):
        factors.append(i)

arr = part(S, k)
flag = -1
#print(part(S, k))

for i in arr:
    temp = i
    cnt = 0; prod = 1

    for j in temp:
        if(j in factors):
            cnt += 1
        prod *= j

    if(cnt == k and prod == P):
        print(*temp)
        flag = 0
        break
    else:
        flag = 1

if(flag != 0):
    print("NO")
