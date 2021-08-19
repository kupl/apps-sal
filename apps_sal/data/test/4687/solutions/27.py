(n, k) = list(map(int, input().split()))
sum_b = 0
ab_list = []
for i in range(n):
    ab_list.append(list(map(int, input().split())))
ab_list.sort()
for i in range(n):
    (a, b) = ab_list[i]
    sum_b += b
    if sum_b >= k:
        print(a)
        break
