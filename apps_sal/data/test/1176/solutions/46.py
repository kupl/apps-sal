n = int(input())
a = list(map(int, input().split()))
b = []
cnt = 0
for i in range(n):
    b.append(abs(a[i]))
    if a[i] < 0:
        cnt += 1
if cnt % 2 == 0:
    print(sum(b))
else:
    print(sum(b)-min(b)*2)
