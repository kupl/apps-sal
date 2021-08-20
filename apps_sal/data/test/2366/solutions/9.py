n = int(input())
a = list(map(int, input().split()))
x = [0] * (n + 1)
for i in a:
    x[i] += 1
ans = 0
for i in x:
    n = i
    ans += n * (n - 1) // 2
for i in a:
    n = x[i]
    ans1 = ans - (n - 1)
    print(ans1)
