n = int(input())
a, b = map(int, input().split())
ans = "NG"
for i in range(a, b + 1):
    if i % n == 0:
        ans = "OK"
        break
print(ans)
