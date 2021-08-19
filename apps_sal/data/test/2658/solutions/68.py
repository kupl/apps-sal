n, k = list(map(int, input().split()))
a = list(map(int, input().split()))


def index_multi(l, x):
    return [i for i, _x in enumerate(l) if _x == x]


t = 0
lis = [1]
count = [0] + [-1] * (n - 1)  # 到達回数
for i in range(2 * (10 ** 5) + 1):
    lis.append(a[t])
    t = a[t] - 1
    count[t] += 1
# print(lis)
# print(count)
l_start_number = 0
for i in range(n):
    if count[i] > 0:
        l_start_number = i + 1
        break

l_start = index_multi(lis, l_start_number)[0]
l_goal = index_multi(lis, l_start_number)[1] - 1

loop_lis = []
for i in range(l_start, l_goal + 1):
    loop_lis.append(lis[i])
# print(loop_lis)

loop = len(loop_lis)
if k >= l_start:
    count = (k - l_start) % loop
    print((loop_lis[count]))
else:
    print((lis[k]))
