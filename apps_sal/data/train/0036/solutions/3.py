

input()
heaps = list(map(int, input().split()))
input()
numbers = list(map(int, input().split()))
res = [0] * len(numbers)

sums = [heaps[0]]
mask = [1] * heaps[0]
for i in range(1, len(heaps)):
    mask += [i + 1] * (heaps[i])
    sums.append(heaps[i] + sums[-1])

for i in range(len(numbers)):
    print(mask[numbers[i] - 1])
