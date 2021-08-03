from collections import Counter

N = int(input())
A = list(map(int, input().split()))


count = Counter(A)
select_num = [0] * (10 ** 6 + 1)

for num, cnt in Counter(A).items():
    select_num[num] = cnt * (cnt - 1) // 2

sum_select = sum(select_num)

for a in A:
    print(sum_select - select_num[a] + (count[a] - 1) * (count[a] - 2) // 2)
