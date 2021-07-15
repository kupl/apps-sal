n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_per = n * [0]
for i in range(n):
    a_per[a[i] - 1] = i

cur_moved = -1
for i in range(n):
    print(max(a_per[b[i] - 1] - cur_moved, 0), end = " ")
    cur_moved = max(cur_moved, a_per[b[i] - 1])

