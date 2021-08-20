from heapq import heappush, heappushpop
N = int(input())
a = list(map(int, input().split()))
a_list_1 = []
a_list_2 = []
for i in a[0:N]:
    heappush(a_list_1, i)
for i in list(reversed(a))[0:N]:
    heappush(a_list_2, -i)
sum_1 = sum(a_list_1)
sum_2 = sum(a_list_2)
sum_arr_1 = [0] * (N + 1)
sum_arr_1[0] = sum_1
sum_arr_2 = [0] * (N + 1)
sum_arr_2[-1] = sum_2
for k in range(N, 2 * N):
    l = heappushpop(a_list_1, a[k])
    sum_1 += a[k] - l
    sum_arr_1[k - N + 1] = sum_1
for k in reversed(range(N, 2 * N)):
    l = heappushpop(a_list_2, -a[k])
    sum_2 += -a[k] - l
    sum_arr_2[k - N] = sum_2
max_score = float('-inf')
for (s1, s2) in zip(sum_arr_1, sum_arr_2):
    score = s1 + s2
    if score > max_score:
        max_score = score
print(max_score)
