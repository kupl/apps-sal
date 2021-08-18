def R(): return list(map(int, input().split()))


n = int(input())
a = list(R())
a.sort()
x, c = a[0], 3
if n == 3 or a[2] < a[3]:
    print("1")
    return
elif a[1] < a[2]:
    x = a[2]
    c = 1
elif a[0] < a[1]:
    x = a[1]
    c = 2
t = sum(x == y for y in a)
f = 1
for i in range(c):
    f = f * (t - i) / (i + 1)
print(int(f))
