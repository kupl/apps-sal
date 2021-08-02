n = int(input())
l = list(map(int, input().split()))
l_sum = sum(l)
c_sum = [0 for _ in range(n)]
total = 0

mid = None
for i, x in enumerate(l):
    total += x
    c_sum[i] = total
    if mid is None and total >= l_sum // 2:
        mid = i

point_left = mid
point_right = mid + 1
sum_left = c_sum[mid]
sum_right = total - c_sum[mid]

while sum_left != sum_right:
    if point_left < 0:
        break
    if point_right >= n:
        break

    if sum_left > sum_right:
        sum_left -= l[point_left]
        point_left -= 1
    else:
        sum_right -= l[point_right]
        point_right += 1


print(min(sum_left, sum_right))
