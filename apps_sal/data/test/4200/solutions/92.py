n,m = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
cnt = 0
for i in range(n):
    if a[i]*4*m >= s:
        cnt += 1
if cnt >= m:
    print("Yes")
else:
    print(("No"))
