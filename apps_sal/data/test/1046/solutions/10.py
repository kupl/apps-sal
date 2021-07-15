t = int(input())
sec = list(map(int, input().split()))
total = 0
m = set(sec)
for i in m:
    if i == 0:
        continue
    if sec.count(i) > 2:
        print(-1)
        return
    if sec.count(i) == 2:
        total += 1
print(total)
