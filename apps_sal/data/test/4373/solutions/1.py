n = int(input())
l = sorted(map(int, input().split()))
i = 0
res = 0
while i < n:
    if res < l[i]:
        res += 1
    i += 1
print(res)
