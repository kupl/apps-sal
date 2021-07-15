n = int(input())
p = list(map(int, input().split()))
total = 0
cnt = 0
for idx, value in enumerate(p, start=1):
    if idx == value:
        cnt += 1
    elif idx != value and cnt != 0:
        if cnt % 2 == 1:
            total += cnt // 2 + 1
        else:
            total += cnt // 2
        cnt = 0
if cnt % 2 == 1:
    total += cnt // 2 + 1
else:
    total += cnt // 2
print(total)
