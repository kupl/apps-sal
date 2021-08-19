N = int(input())
t = N // 2
a_list = []
b_list = []
for i in range(N):
    ab = list(map(int, input().split()))
    a_list.append(ab[0])
    b_list.append(ab[1])
a_list = sorted(a_list)
b_list = sorted(b_list)
if N % 2 == 1:
    a_median = a_list[t]
    b_median = b_list[t]
    print(b_median - a_median + 1)
elif N % 2 == 0:
    a_median = (a_list[t - 1] + a_list[t]) / 2
    b_median = (b_list[t - 1] + b_list[t]) / 2
    print(int(2 * (b_median - a_median) + 1))
