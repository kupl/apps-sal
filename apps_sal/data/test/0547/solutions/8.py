n, k = map(int, input().split())
a = []
for i in range(n):
    s = input().rstrip()
    a.append((len(s), s))
s1 = input().rstrip()
a.sort()
time = 0
ans1 = ans2 = 10 ** 13
for i in range(n):
    time += 1
    if a[i][0] == len(s1):
        ans1 = min(ans1, time)
    if i == n - 1 or a[i + 1][0] > len(s1):
        ans2 = min(ans2, time)
    if (i + 1) % k == 0:
        time += 5
ans2 = min(ans2, time)
print(ans1, ans2)
