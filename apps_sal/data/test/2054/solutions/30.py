T = int(input())
for cas in range(T):
    ans = 0
    a,b = map(int,input().split())
    if a * 2 <= b:
        ans = a
    elif b * 2 <= a:
        ans = b
    else:
        ans = (a + b) // 3
    print(ans)
