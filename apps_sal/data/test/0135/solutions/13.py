(n, k) = list(map(int, input().split()))
ans = 'Yes'
for i in range(2, k + 1):
    if n % i != i - 1:
        ans = 'No'
        break
    elif 1000000.0 < i:
        break
print(ans)
