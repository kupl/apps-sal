n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] == 1:
        p1 = i
    if a[i] == n:
        pn = i
print(max(abs(p1 - pn), p1, pn, abs(n - 1 - p1), abs(n - 1 - pn)))
