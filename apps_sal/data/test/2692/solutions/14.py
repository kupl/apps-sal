# //author : 'Amit Singh Sansoya @amit3200'
# //it was all meant to happen as i was all talk!
def finder(k):
    eaten = 0
    crumbs = 0
    while k > 0:
        eaten += k
        crumbs += k
        k = crumbs // b
        crumbs %= b
    return eaten


def search(N):
    lo = 1
    hi = N
    while lo < hi:
        mid = (lo + hi) // 2
        total = finder(mid)
        if total < n:
            lo = mid + 1
        else:
            hi = mid
    print(hi)


for _ in range(int(input())):
    n, b = list(map(int, input().split()))
    search(n)
