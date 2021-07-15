n = int(input())

cnt = [0] * 101

for x in range(n):
    lst = [int(y) for y in input().split()]

    for i in range(1, len(lst)):
        cnt[lst[i]] += 1

for x in range(1, 101):
    if cnt[x] == n:
        print(x, end = ' ')
    


