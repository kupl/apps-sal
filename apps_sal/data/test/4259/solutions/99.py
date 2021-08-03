k = int(input())
a, b = list(map(int, input().split()))
n = 0
for i in range(a, b + 1):
    if i % k == 0:
        n = 1
        break

if n == 1:
    print("OK")
else:
    print("NG")
