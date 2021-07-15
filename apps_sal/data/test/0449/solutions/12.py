n = int(input())
arr = [100, 20, 10, 5, 1]
ans = 0
for i in range(5):
    ans += n // arr[i]
    n = n % arr[i]
print(ans)
