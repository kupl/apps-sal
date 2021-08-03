pref = [2]
for i in range(2, 30000):
    pref.append(i * 3 - 1)
    pref[-1] += pref[-2]
t = int(input())

for uuu in range(t):
    n = int(input())
    cnt = 0
    while(n > 1):
        l = 0
        r = 30000
        while(r - l > 1):
            mid = (r + l) // 2
            if(pref[mid] > n):
                r = mid
            else:
                l = mid
        n -= pref[l]
        cnt += 1
    print(cnt)
