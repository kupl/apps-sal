n = int(input())
a = [0]
for i in range(n):
    a.append(int(input()))
cnt = 0
a_before = 1
while cnt <= n:
    cnt += 1
    if a[a_before] == 2:
        print(cnt)
        break
    a_before = a[a_before]
else:
    print(-1)
