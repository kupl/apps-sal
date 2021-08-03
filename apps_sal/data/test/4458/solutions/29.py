n = int(input())

lst = [int(i) for i in input().split()]
mn = lst[0]
count = 0
for d in lst:
    if mn >= d:
        count += 1
        mn = d

print(count)
