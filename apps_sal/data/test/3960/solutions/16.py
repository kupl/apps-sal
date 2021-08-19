input()
numbers = [int(x) for x in input().split()]
diffs = []
(sum_odd, sum_even) = (0, 0)
for x in range(len(numbers) - 1):
    diffs.append(abs(numbers[x] - numbers[x + 1]))
_max = 0
for x in range(len(diffs)):
    aux = diffs[x]
    if x % 2 == 1:
        aux *= -1
    sum_even += aux
    sum_odd -= aux
    if sum_even < 0:
        sum_even = 0
    if sum_odd < 0:
        sum_odd = 0
    _max = max([sum_even, sum_odd, _max])
print(_max)
