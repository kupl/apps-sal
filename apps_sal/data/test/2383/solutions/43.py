n = int(input())
a_l = list(map(int, input().split()))
ans = 0
i = 0
j = 0
while i < n:
    if a_l[i] == j + 1:
        j += 1
        i += 1
        continue
    ans += 1
    i += 1
if ans > n - 1:
    print('-1')
else:
    print(ans)
