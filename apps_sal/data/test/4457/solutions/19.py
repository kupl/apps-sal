n = int(input())
li = list(map(int, input().split()))
d = {}
b = []
for i in range(1, n + 1):
    k = li[i - 1]
    try:
        d[k].append(i)
    except KeyError:
        d[k] = [i]
        b.append(k)
b.sort(reverse=True)
ans1 = []
ans = 0
l = 0
for i in b:
    for j in d[i]:
        ans1.append(j)
        ans += l * i + 1
        l += 1
print(ans)
print(*ans1)
