n = int(input())
x = list(map(int, input().split()))
ans = sorted(x)
ans2 = ans[n // 2 - 1]
ans1 = ans[n // 2]

for i in range(n):
    if x[i] >= ans[n // 2]:
        print(ans2)
    else:
        print(ans1)
