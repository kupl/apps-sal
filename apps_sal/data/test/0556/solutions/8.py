(l, r, k) = map(int, input().split())
curk = 1
while curk < l:
    curk *= k
ans = 0
while curk <= r:
    ans += 1
    print(curk, end=' ')
    curk *= k
if not ans:
    print(-1)
else:
    print()
