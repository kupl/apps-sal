N = input()
a = list(map(int, input().split()))
res = 10 ** 9
for i in a:
    count = 0
    while i % 2 == 0:
        count += 1
        i = i / 2
    if count < res:
        res = count
print(res)
