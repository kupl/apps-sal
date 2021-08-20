def merge(l1, l2):
    p1 = 0
    p2 = 0
    l = []
    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] < l2[p2]:
            l.append(l1[p1])
            p1 += 1
        else:
            l.append(l2[p2])
            p2 += 1
    if p1 < len(l1):
        l.extend(l1[p1:len(l1)])
    if p2 < len(l2):
        l.extend(l2[p2:len(l2)])
    return l


def merge_sort(l):
    if len(l) == 1:
        return l
    else:
        l1 = merge_sort(l[0:len(l) // 2])
        l2 = merge_sort(l[len(l) // 2:len(l)])
        return merge(l1, l2)


n = int(input())
dist_str = input()
first_dist = list([int(s) for s in dist_str.split(' ')])
m = int(input())
dist_str = input()
second_dist = list([int(s) for s in dist_str.split(' ')])
first_dist.sort()
second_dist.sort()
first_sum = 3 * n
second_sum = 3 * m
diff = first_sum - second_sum
thr_p1 = 0
thr_p2 = 0
first_sum_temp = first_sum
second_sum_temp = second_sum
diff_temp = diff
while thr_p1 < n and thr_p2 < m:
    if first_dist[thr_p1] < second_dist[thr_p2]:
        first_sum_temp -= 1
        thr_p1 += 1
    elif first_dist[thr_p1] > second_dist[thr_p2]:
        second_sum_temp -= 1
        thr_p2 += 1
    else:
        first_sum_temp -= 1
        second_sum_temp -= 1
        thr_p2 += 1
        thr_p1 += 1
    diff_temp = first_sum_temp - second_sum_temp
    if diff_temp > diff:
        diff = diff_temp
        first_sum = first_sum_temp
        second_sum = second_sum_temp
while thr_p1 < n:
    first_sum_temp -= 1
    thr_p1 += 1
    diff_temp = first_sum_temp - second_sum_temp
    if diff_temp > diff:
        diff = diff_temp
        first_sum = first_sum_temp
        second_sum = second_sum_temp
while thr_p2 < m:
    second_sum_temp -= 1
    thr_p2 += 1
    diff_temp = first_sum_temp - second_sum_temp
    if diff_temp > diff:
        diff = diff_temp
        first_sum = first_sum_temp
        second_sum = second_sum_temp
ans = str(first_sum) + ':' + str(second_sum)
print(ans)
