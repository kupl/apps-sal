n = int(input())
ans = []
count = 1
two = 1
for i in range(20):
    if two * 2 <= n:
        count += 1
        ans.append([count - 1, count, 0])
        ans.append([count - 1, count, two])
        two *= 2
    else:
        break

for i in range(count, 0, -1):
    if n - pow(2, i - 1) >= two:

        ans.append([i, count, n - pow(2, i - 1)])
        n -= pow(2, i - 1)
print((count, len(ans)))
for i in ans:
    print((*i))
