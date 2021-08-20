(n, a, b) = (int(i) for i in input().split())
ans = (a + b) % n
if ans == 0:
    print(n)
else:
    print(ans)
