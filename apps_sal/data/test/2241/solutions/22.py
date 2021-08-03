def great_sum_finder(num, rang):
    if abs(num - rang) > rang or num == 1:
        return -1
    if rang == 1:
        return 1
    if num < rang:
        return great_sum_finder(num, num - 1)
    return (num // 2) * (num - num // 2)


n = int(input())
a = input().split()
b = input().split()
a = list(map(int, a))
b = list(map(int, b))
joy = 0
for i in range(n):
    joy += great_sum_finder(b[i], a[i])
print(joy)
