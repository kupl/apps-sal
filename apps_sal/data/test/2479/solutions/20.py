def search(L, x):
    low, high = 0, len(L) - 1
    while low < high:
        mid = (low + high) // 2
        if L[mid + 1] < x < L[mid]:
            return mid
        elif x < L[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low


N, Q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(Q)]
B = [N - 1]
Bv = [N - 2]
R = [N - 1]
Rv = [N - 2]
ans = (N - 2)**2
for f, x in query:
    x -= 1
    if f == 1:
        a = search(R, x)
        ans -= Rv[a]
        if R[-1] >= x:
            Bv[-1] = x - 1
            R.append(x)
            Rv.append(Rv[-1])
    else:
        a = search(B, x)
        ans -= Bv[a]
        if B[-1] >= x:
            Rv[-1] = x - 1
            B.append(x)
            Bv.append(Bv[-1])

print(ans)
