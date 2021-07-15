n = int(input())
tmp = 0
for i in range(1, n + 1):
    tmp += i
    if tmp >= n:
        print(i)
        break
