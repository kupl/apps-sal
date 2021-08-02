N, M = map(int, input().split())
n = list(map(int, input().split()))
m = list(map(int, input().split()))
count = 0
for i in n:
    if len(m) == 0:
        break
    if m[0] >= i:
        count += 1
        m.pop(0)
print(count)
