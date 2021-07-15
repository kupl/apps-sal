m, k = map(int, input().split())
if 2**m <= k:
    print(-1)
    return
elif m == 0 and k == 0:
    print("0 0")
    return
elif m == 1 and k == 1:
    print(-1)
    return
elif m == 1 and k == 0:
    print("1 1 0 0")
    return
l = [i for i in range(2**m) if i != k]
rev_l = sorted(l, reverse=True)
ans = l + [k] + rev_l + [k]
print(" ".join(map(str, ans)))
