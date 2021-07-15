n = int(input())
a = [int(i) for i in input().split()]
for i in range(n // 2):
    a[i] -= 1
ans1 = 0
ans2 = 0
a.sort()
for i in range(n // 2):
    ans1 += abs(a[i] - 2 * i)
    ans2 += abs(a[i] - 2 * i - 1)
print(min(ans1, ans2))

