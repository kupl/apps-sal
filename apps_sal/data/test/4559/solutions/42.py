n = input()
a = list(map(int, input().split()))
a.sort()
p = 1
if a[0] == 0:
    ans = 0
else:
    for i in a:
        p *= i
        if p > 10 ** 18:
            ans = -1
            break
        ans = p
print(ans)
