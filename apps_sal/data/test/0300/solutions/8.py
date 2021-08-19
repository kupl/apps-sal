n = int(input())
a = sorted(list(map(int, input().split())))
for i in range(n + 1):
    cur_sum = 5 * i + sum(a[i:])
    if cur_sum * 10 >= n * 45:
        print(i)
        break
