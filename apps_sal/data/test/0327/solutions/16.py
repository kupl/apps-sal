(n, k) = list(map(int, input().split()))
if k == 1:
    print(n)
else:
    ans = bin(n)[2:]
    ans = ans.replace('0', '1')
    ans = int(ans, 2)
    print(ans)
