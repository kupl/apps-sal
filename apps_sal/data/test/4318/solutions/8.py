n = int(input())
li = list(map(int, input().split()))
cnt = 0
min = li[0]
for i in li:
    if i >= min:
        cnt += 1
        min = i
print(cnt)
