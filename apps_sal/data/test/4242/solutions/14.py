# https://atcoder.jp/contests/abc120/tasks/abc120_b

a, b, k = map(int, input().split())

min_a_b = min(a, b)
divisor_list = []

for i in range(1, min_a_b + 1):
    if a % i == 0 and b % i == 0:
        divisor_list.append(i)

divisor_list.sort(reverse=True)
print(divisor_list[k - 1])
