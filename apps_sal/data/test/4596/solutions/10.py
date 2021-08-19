n = int(input())
a = list(map(int, input().split()))
cnt = 0
while True:
    exist_odd = False
    for index in range(len(a)):
        if a[index] % 2 != 0:
            exist_odd = True
        a[index] /= 2
    if exist_odd:
        break
    cnt = cnt + 1
print(cnt)
