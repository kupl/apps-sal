n = int(input())
arr = input().split(' ')
last_zeros = [0] * n
last_zero = -1
for i in range(n):
    arr[i] = int(arr[i])
    if arr[i] == 0:
        last_zero = i
    if last_zero == -1:
        last_zeros[i] = 10 ** 10
    else:
        last_zeros[i] = i - last_zero
last_zero = -1
for i in reversed(range(n)):
    if arr[i] == 0:
        last_zero = i
    if last_zero != -1:
        last_zeros[i] = min(last_zeros[i], last_zero - i)
for el in last_zeros:
    print(el, end=' ')
