n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = a[0]
if n == 2:
    print(ans)
elif n % 2 == 0:
    ans += sum(a[1:n // 2]) * 2
    print(ans)
else:
    ans += sum(a[1:n // 2]) * 2
    ans += a[n // 2]
    print(ans)
