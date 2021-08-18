
n = input()
s = list(input().split())

i = 1
l = list()
for x in s:
    l.append((int(x), i))
    i += 1
l.sort()
ans = 0
for i in range(1, len(l)):
    ans += abs(l[i][1] - l[i - 1][1])

print(ans)
