a = input()
a = a.split(' ')
a = list(map(int,a))
def really_big(n,s):
    if s >= n:
        return 0
    i = s + 1
    while i <= n:
        t,b = i,0
        while t > 0:
            b = b + (t % 10)
            t = t // 10
        if i - b >= s:
            return n - i + 1
            break
        else:
            i += 1
    return 0
print(really_big(a[0],a[1]))
