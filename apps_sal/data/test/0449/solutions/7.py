n = int(input())

cnt = 0

ls = [100, 20, 10, 5, 1]

for i in ls:
    if n == 0:
        break
    cnt += n // i
    n = n % i

print(cnt)
