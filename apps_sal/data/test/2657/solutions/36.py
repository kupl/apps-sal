N = int(input())
a = list(map(int, input().split()))
ma = max(a)
a.remove(ma)
num = 0
ind = 0
a.sort()
for i in range(N - 1):
    if a[i] < ma // 2:
        ind += 1

if ind == 0:
    print(ma, a[0])
    return
elif ind == N - 1:
    print(ma, a[-1])
    return

if abs(ma // 2 - a[ind - 1]) < abs(ma // 2 - a[ind]):
    print(ma, a[ind - 1])
else:
    print(ma, a[ind])
