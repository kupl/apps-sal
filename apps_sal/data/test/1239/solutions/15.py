N = int(input())
array = list(map(int, input().split()))
array.sort()
minimum = abs(array[0] - array[-1])
ans_amount = 0
for i in range(N - 1):
    if array[i + 1] - array[i] < minimum:
        ans_amount = 1
        minimum = array[i + 1] - array[i]
    elif array[i + 1] - array[i] == minimum:
        ans_amount += 1
print(minimum, end=' ')
print(ans_amount)
