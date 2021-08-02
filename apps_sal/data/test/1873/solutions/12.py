n, m = list(map(int, input().split()))
l = list(map(int, input().split()))
num = [0] * int(2 * 1e5 + 5)
for i in l:
    num[i] += 1
ans = n * (n - 1) // 2
for i in num:
    ans -= i * (i - 1) // 2
print(ans)
