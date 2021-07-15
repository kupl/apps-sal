n = int(input())
t_lst = list(map(int, input().split()))
m = int(input())

for i in range(m):
    p, x = list(map(int, input().split()))
    count = 0
    for j in range(n):
        if j == p-1:
            count += x
        else:
            count += t_lst[j]
    print(count)


