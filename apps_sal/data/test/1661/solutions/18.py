n, m = map(int, input().split())
a = [int(elem) for elem in input().split()]
b = [int(elem) for elem in input().split()]
ans = 0
for i in range(n):
    if len(b) > 0 and a[i] <= b[0]:
        b = b[1:]
        ans = ans + 1
print(ans)
