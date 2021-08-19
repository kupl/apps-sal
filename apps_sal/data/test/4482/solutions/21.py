N = int(input())
a = list(map(int, input().split()))


def my_round_int(x):
    return int((x * 2 + 1) // 2)


m = my_round_int(sum(a) / len(a))
cost = 0
for i in a:
    cost += (i - m) ** 2
print(cost)
