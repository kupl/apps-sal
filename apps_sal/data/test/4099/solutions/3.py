n, k, m = map(int, input().split())
a = map(int, input().split())

score = sum(a)

for i in range(k + 1):
    total = score + i
    avarage = total / n
    if avarage >= m:
        print(i)
        break
    if i == k:
        print('-1')
