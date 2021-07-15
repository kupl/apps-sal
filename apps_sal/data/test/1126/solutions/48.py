n, x, m = map(int, input().split())
list_A = [x]
set_A = {x}
while True:
    a = pow(list_A[-1], 2, m)
    if a in set_A:
        break
    list_A.append(a)
    set_A.add(a)

if len(list_A) >= n:
    print(sum(list_A[:n]))
else:
    k = list_A.index(a)
    s = sum(list_A[k:])
    l = len(list_A) - k

    h = (n - len(list_A)) // l
    g = (n - len(list_A)) % l

    ans = sum(list_A) + h * s + sum(list_A[k:k + g])

    print(ans)
