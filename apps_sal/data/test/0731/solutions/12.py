w, m, k = input().split()
k = int(w) // int(k)
l, m = len(m), int(m)
s = pow(10, l)
if (s - m) * l > k: print(k // l)
else:
    k -= (s - m) * l
    l += 1
    d = 9 * s
    while d * l <= k:
        k -= d * l
        l += 1        
        s += d
        d = 9 * s
    print(s - m + k // l)
