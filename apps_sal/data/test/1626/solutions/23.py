mask = 10 ** 9 + 7


def count(a, x):
    return x // a + 1


(n, k) = list(map(int, input().split()))
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))
big = 10 ** k - 1
small = 10 ** (k - 1)
result = 1
for i in range(n // k):
    (a, b) = (aa[i], bb[i])
    sum = 0
    sum += count(a, big)
    sum -= count(a, (b + 1) * small - 1)
    if b != 0:
        sum += count(a, b * small - 1)
    result = result * sum % mask
print(result)
