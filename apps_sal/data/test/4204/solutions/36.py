s = input()
k = int(input())
cnt = 0
for i in s:
    if i == '1':
        cnt += 1
    else:
        x = i
        break
if cnt >= k:
    print(1)
else:
    print(x)
