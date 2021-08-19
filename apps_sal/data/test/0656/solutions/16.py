(n, k) = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]
colddays = [i for i in range(n) if t[i] < 0]
num_colddays = len(colddays)
if num_colddays == 0:
    print(0)
elif k >= n:
    print(1)
elif num_colddays > k:
    print(-1)
else:
    k -= num_colddays
    ans = 0
    for i in range(1, len(colddays)):
        if colddays[i] - colddays[i - 1] > 1:
            ans += 1
    ans += 1
    ans *= 2
    gap = [0 for i in range(num_colddays)]
    for j in range(1, num_colddays):
        gap[j - 1] = colddays[j] - colddays[j - 1] - 1
    positivegap = [j for j in gap if j > 0]
    positivegap = sorted(positivegap)
    for i in positivegap:
        if k >= i:
            k -= i
            ans -= 2
        else:
            break
    remain = n - 1 - colddays[-1]
    if k >= remain:
        ans -= 1
    print(ans)
