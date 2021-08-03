n, k = map(int, input().split())
s = input()
chars = set(map(str, input().split()))

total = 0

cur = 0
for i in s:
    if i in chars:
        cur += 1
    else:
        if cur != "":
            total += cur * (cur + 1) // 2
        cur = 0

if cur != 0:
    total += cur * (cur + 1) // 2


print(total)
