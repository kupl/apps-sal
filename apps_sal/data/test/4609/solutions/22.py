n = int(input())
a = {}
cnt = 0
for i in range(n):
    num = int(input())
    a[num] = a.get(num, 0) + 1
    a[num] %= 2
for i in a.values():
    cnt += i
print(cnt)
