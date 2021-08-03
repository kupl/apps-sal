k = int(input())

a, b = input().split()

ans = 0
for i in range(int(a), int(b) + 1):
    if i % k == 0:
        ans = 1

if ans == 1:
    print("OK")
else:
    print("NG")
