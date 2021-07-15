N = input()
N = int(N)
li = []
for i in range(N):
    li.append(input())

ans = 0
a = []
b = 0
for i in range(101):
    a.append(i - i)

for i in range(N):
    b = li[i]
    b = int(b)
    a[b] = 1

for i in range(101):
    ans += a[i]
print(ans)
