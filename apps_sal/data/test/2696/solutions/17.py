n = int(input())
a = [int(x) for x in input().split()]
ans = n-1
x = a[-1]
while ans-1 >= 0:
    if a[ans-1] == x:
        x = a[ans-1]
        ans -= 1
    else:
        break
print(ans+1)

