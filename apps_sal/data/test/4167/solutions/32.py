n,k = map(int,input().split())
if k % 2 == 1:
    ans = (n // k) ** 3
if k % 2 == 0:
    mk2 = n // (k //2)
    mk = n // k
    ans = mk ** 3 + (mk2 - mk) ** 3
print(ans)
