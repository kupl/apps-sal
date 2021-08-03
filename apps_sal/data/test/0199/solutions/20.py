n, k = list(map(int, input().split(' ')))

a = list(map(int, input().split(' ')))

minV = min(a)

s = sum(a)

if(k > s):
    print(-1)
else:
    rest = s - minV * n
    if(rest >= k):
        print(minV)
    else:
        k -= rest

        sol = k // n
        if(k % n):
            sol += 1

        print(minV - sol)
