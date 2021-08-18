n, k = map(int, input().split())
h = list(map(int, input().split()))
able_num = 0
for i in h:
    if i >= k:
        able_num += 1
print(able_num)
