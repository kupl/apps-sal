n = int(input())
a = list(map(int, input().split(" ")))
a_max = 0
step = 0

for i in range(n):
    if a_max < a[i]:
        a_max = a[i]
        a_num = i
    else:
        step += a_max - a[i]

print(step)
