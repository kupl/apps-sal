n = int(input())
a = list(map(int, input().split()))
max_el = -1
er = -1
for i in range(len(a)):
    if a[i] - max_el > 1:
        er = i + 1
        break
    if a[i] > max_el:
        max_el = a[i]

print(er)
