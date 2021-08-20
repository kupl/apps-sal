def main(n, d):
    p = []
    for i in range(n):
        (a, b) = list(map(int, input().split()))
        p.append([a, b])
    p.sort()
    maxi = 0
    sum = 0
    e = []
    g = 0
    em = 0
    while len(p) != 0:
        while g != n and p[g][0] < p[em][0] + d:
            sum += p[g][1]
            g += 1
        if g == n:
            maxi = max(maxi, sum)
            print(max(maxi, sum))
            break
        else:
            maxi = max(maxi, sum)
            while em != g and p[em][0] + d <= p[g][0]:
                sum -= p[em][1]
                em += 1


(n, d) = list(map(int, input().split()))
main(n, d)
