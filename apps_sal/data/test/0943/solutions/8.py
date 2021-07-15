N = int(input())
a = list(map(int, input().split()))
k = 0
min_nechet = 10 ** 10
for i in a:
    if i % 2 == 1:
        k += 1
        min_nechet = min(min_nechet, i)
if k % 2 == 0:
    print(sum(a))
else:
    print(sum(a) - min_nechet)
