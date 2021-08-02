n = int(input())
p = list(map(int, input().split()))

cnt = 0
increased = False
for i in range(n):
    if increased:
        increased = False
        continue

    if p[i] == i + 1:
        cnt += 1
        i += 1
        increased = True

print(cnt)
