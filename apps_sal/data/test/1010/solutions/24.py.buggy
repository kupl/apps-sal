n = int(input())
a = list(map(int, input().split()))
if max(a) == 0:
    print(0)
    return
ans = 1
started = False
count = 1
for i in range(n):
    if a[i] == 1 and not started:
        started = True
        continue
    if started and a[i] == 0:
        count += 1
    if started and a[i] == 1:
        ans *= count
        count = 1
print(ans)
