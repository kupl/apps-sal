def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    n = int(input())
    a_1 = Input()
    a_2 = Input()
    a_1_sum = [0] * n
    a_2_sum = [0] * n
    a_1_sum[0] = a_1[0]
    for i in range(1, n):
        a_1_sum[i] = a_1_sum[i - 1] + a_1[i]
    for i in range(n):
        a_2_sum[i] = sum(a_2) - sum(a_2[:i])
    ans = 0
    for (a1, a2) in zip(a_1_sum, a_2_sum):
        ans = max(ans, a1 + a2)
    print(ans)


main()
