(n, v) = map(int, input().split())
sumi = 0
ls = []
for i in range(n):
    li = list(map(int, input().split()))
    for j in range(1, len(li)):
        if v > li[j]:
            sumi = sumi + 1
            ls.append(i + 1)
            break
print(sumi)
if sumi != 0:
    print(' '.join(map(str, ls)))
