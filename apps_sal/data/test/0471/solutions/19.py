n, d = map(int, input().split())
a = list(map(int, input().strip().split()))

# print(n)
# print(a)
a.sort()
# print(a)

ans = 0
if n == 1:
    ans = 0
elif n <= 2:
    ans = min(abs(a[0] - d), abs(a[n - 1] - d))
else:
   # print("en")
    ans = a[n - 2] - a[0] + min(abs(a[0] - d), abs(a[n - 2] - d))
    # print(ans)
    ans = min(ans, a[n - 1] - a[1] + min(abs(a[1] - d), abs(a[n - 1] - d)))
   # print(ans)
print(ans)
