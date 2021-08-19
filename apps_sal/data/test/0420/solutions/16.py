def readln():
    return tuple(map(int, input().split()))


(n, m) = readln()
a = [readln() for _ in range(n)]
ans = n
while ans % 2 == 0:
    p1 = a[:ans // 2]
    p2 = a[ans // 2:]
    p2.reverse()
    if p1 != p2:
        break
    a = p1
    ans //= 2
print(ans)
