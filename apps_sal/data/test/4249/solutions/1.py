[n, m] = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort(reverse=True)
def check (i):
    mins = 0
    cnt = 0
    sums = 0
    for x in arr:
        sums += max(x-mins,0)
        if sums >= m:
            return True
        cnt += 1
        if cnt >= i:
            cnt = 0
            mins += 1
    return False

l = 1
r = n+1
while l!= r:
    if check((l+r)//2) :
        r = (l+r)//2
    else:
        l = (l+r)//2+1

print(l if l > 0 and l <= n else -1)
