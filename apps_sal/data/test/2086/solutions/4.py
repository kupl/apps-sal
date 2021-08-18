
def ps(l, i, j):
    if i > j:
        return l[-1] - l[i - 1] + l[j]
    if i == 0:
        return l[j]
    else:
        return l[j] - l[i - 1]


n = int(input())
a = list(map(int, input().split()))
s, f = map(int, input().split())

l = [a[0]]
for i in a[1:]:
    l.append(l[-1] + i)
x = s - 1
y = f - 2
ans = 0
tm = 0
for i in range(n):
    temp = ps(l, x, y)
    if temp > ans:
        tm = i + 1
        ans = temp
    x -= 1
    y -= 1
    if x < 0:
        x = n - 1
    if y < 0:
        y = n - 1
print(tm)
