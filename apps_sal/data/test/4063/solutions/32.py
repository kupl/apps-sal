n = int(input())
d = list(map(int, input().split()))
d.sort()
abc = d[n // 2 - 1]
arc = d[n // 2]
if abc == arc:
    ans = 0
else:
    ans = arc - abc
print(ans)
