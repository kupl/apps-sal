n = input()
a = sorted(map(int, input().split()))
(ans, time) = (0, 0)
for ii in a:
    if ii >= time:
        ans += 1
        time += ii
print(ans)
