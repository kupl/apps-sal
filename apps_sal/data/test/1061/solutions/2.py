3

array = [list(map(int, input().split())) for _ in range(5)]
i = [_ for _ in range(5) if 1 in array[_]][0]
array = list(zip(*array))
j = [_ for _ in range(5) if 1 in array[_]][0]
print(abs(i - 2) + abs(j - 2))

