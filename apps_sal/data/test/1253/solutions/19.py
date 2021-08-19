def solution():
    (n, k) = [int(x) for x in input().split(' ')]
    l = [int(x) for x in input().split(' ')]
    l = sorted(l, key=lambda x: -abs(x))
    ans = 0
    nbrTrans = 0
    for i in range(n):
        if nbrTrans < k and l[i] < 0:
            nbrTrans += 1
            ans += abs(l[i])
        else:
            ans += l[i]
    sign = 1 if l[n - 1] > 0 else -1
    while k > nbrTrans:
        ans -= 2 * sign * l[n - 1]
        nbrTrans += 1
        sign *= -1
    return ans


print(solution())
