n = int(input())
a = list(input())
ans = ''
pos = 0
count = 1
while pos < n:
    ans += a[pos]
    for i in range(count):
        pos += 1
    count += 1
print(ans)
