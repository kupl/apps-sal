n = int(input())
s = input()
on = []
for i in s:
    if i == '0':
        on.append(0)
    else:
        on.append(1)
a = []
b = []
for i in range(n):
    c, d = map(int, input().strip().split())
    a.append(c)
    b.append(d)
ans = 0
for i in range(300):
    temp = 0
    for j in range(n):
        if i >= b[j]:
            temp += ((i - b[j]) // a[j] + 1 + on[j]) % 2
        else:
            temp += on[j]
    ans = max(temp, ans)
print(ans)
