n = int(input())
a = [int(i) for i in input().split()]
mx = a[0]
ans = 0
for i in a:
    if mx > i:
        ans += mx - i
    elif mx < i:
        mx = i
print(ans)
