(n, k) = map(int, input().split())
arr = []
cnt = 0
for i in range(n):
    (a, b) = map(int, input().split())
    arr.append(a)
    arr.append(b)
    cnt += b - a + 1
m = cnt
if cnt % k == 0:
    print(0)
    quit()
print(k - m % k)
