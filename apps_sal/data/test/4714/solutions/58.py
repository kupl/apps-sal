a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    i = str(i)
    if i[0] == i[-1] and i[1] == i[-2]:
        cnt += 1
print(cnt)
