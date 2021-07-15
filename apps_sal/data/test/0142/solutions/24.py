n, L = list(map(int,input().split()))
arr = [int(x) for x in input().split()]

def pos(x):
    ans = 0
    while(x):
        x //= 2
        ans += 1
    return ans - 1

def solve(ltr):
    if ltr == 0:
        return 0
    val = pos(ltr)
    if val + 1 < n:
        Bmin = min(arr[val + 1:])
    else:
        val = n - 1
        Bmin = 4e20
    minCost = 4e20
    amt = 0
    for i in range(val + 1):
        v = arr[i] / (2 ** i)
        if v <= minCost:
            minCost = v
            amt = i
    minCost = arr[amt]
    minCost *= ltr // (2 ** amt)
    return min(minCost + solve(ltr % ( 2 ** amt)), Bmin)

print(solve(L))

