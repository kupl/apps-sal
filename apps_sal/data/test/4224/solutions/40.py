n = int(input())
cnt = 0
a_list = list(map(int, input().split()))
for i in range(n):
    while True:
        if a_list[i] % 2 == 0:
            cnt += 1
            a_list[i] = a_list[i] / 2
        else:
            break
    cnt = max(cnt, 0)
print(cnt)
