CONST = 10 ** 9 + 7
N = int(input())
numbers = list(map(int, input().split()))
r = 0


def cumsum(xs):
    result = []
    for i in range(len(xs)):
        if i == 0:
            result.append(xs[0])
        else:
            result.append(result[-1] + xs[i])
    return result


numbers.reverse()
num_sum = cumsum(numbers)
num_sum.reverse()
numbers.reverse()
del num_sum[0]
for i in range(N - 1):
    r += (numbers[i] * num_sum[i]) % CONST
print((r % CONST))

