rd = lambda: list(map(int, input().split()))

(n, k), a = rd(), rd()

def proceed(a):
    nonlocal n, k
    
    b = [{} for _ in range(11)]
    
    ans = 0
    for i in range(n - 1, 0, -1):
        cur = a[i] % k
        ln = len(str(a[i]))
    
        if cur not in b[ln]:
            b[ln][cur] = 0
        b[ln][cur] += 1
    
        for j in range(11):
            cur = (k - a[i - 1] * 10 ** j % k) % k
            ans += b[j][cur] if cur in b[j] else 0
    return ans
    

print(proceed(a) + proceed(a[::-1]))
