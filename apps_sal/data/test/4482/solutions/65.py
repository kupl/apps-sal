N = int(input())
a = list(map(int, input().split()))


def calc_cost(x, avg):
    return (x - avg) ** 2


avg = sum(a) // N
delta = [-2, -1, 0, 1, 2]
ans = 10 ** 20
for i in range(len(delta)):
    val = sum(map(lambda x: calc_cost(x, avg + delta[i]), a))
    ans = min(ans, val)
print(ans)
