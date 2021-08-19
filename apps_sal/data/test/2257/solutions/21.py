def square(xx):
    return xx * xx


s = input().split()
n = int(s[0])
x0 = int(s[1])
y0 = int(s[2])
x1 = int(s[3])
y1 = int(s[4])
ans = 0
left = []
right = []
for i in range(0, n):
    s = input().split()
    x = int(s[0])
    y = int(s[1])
    left.append(square(x - x0) + square(y - y0))
    right.append(square(x - x1) + square(y - y1))
    ans = max(ans, right[i])
for i in range(0, n):
    temp = 0
    for j in range(0, n):
        if left[j] > left[i]:
            temp = max(temp, right[j])
    ans = min(ans, temp + left[i])
print(ans)
