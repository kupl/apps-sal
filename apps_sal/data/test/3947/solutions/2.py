
MAXN = 5 * 10**5 + 100
a = []
ans = 0

n = int(input())

a = list(map(int, input().split()))
a.append(0)

a = [0] + a
n = n + 2
arr = []
arr.append(a[0])
arr.append(a[1])


i = 2
while i < n:
    ln = a[i]
    l1 = arr[-1]
    l0 = arr[-2]
    while l1 <= l0 and l1 <= ln:
        ans = ans + min(l0, ln)
        arr.pop()
        l1 = arr[-1]
        l0 = arr[-2]
    arr.append(ln)
    i = i + 1
for i in range(1, len(arr) - 1):
    ans += min(arr[i - 1], arr[i + 1])

print(ans)
