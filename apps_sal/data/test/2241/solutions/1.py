n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0
for i in range(n):
    if 2 * a[i] < b[i]:
        s -= 1
    else:
        x = b[i] // 2
        y = b[i] - x
        if x * y != 0:
            s += x * y
        else:
            s -= 1
print(s)
