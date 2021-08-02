k = int(input())
a, b = list(map(int, input().split()))
for i in range(a, b + 1):
    ans = 'NG'
    if i % k == 0:
        ans = 'OK'
        break
print(ans)
