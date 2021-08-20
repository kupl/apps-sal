(n, m) = list(map(int, input().split()))
sum_a = 0
sum_b = 0
arr = []
for i in range(n):
    (a, b) = list(map(int, input().split()))
    sum_a += a
    sum_b += b
    arr.append(a - b)
if sum_a <= m:
    print(0)
elif sum_b > m:
    print(-1)
else:
    arr.sort(reverse=True)
    ans = 0
    i = 0
    while sum_a > m:
        ans += 1
        sum_a -= arr[i]
        i += 1
    print(ans)
