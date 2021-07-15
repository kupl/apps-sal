s = int(input())
cnt = 0
while s:
    s -= max(map(int, str(s)))
    cnt += 1
print(cnt)
