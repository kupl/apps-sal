n = int(input())
array = list(map(int, input().strip().split()))
lengths = []
curr_length = 0
for i in range(n):
    if array[i] != 0:
        curr_length += 1
    else:
        lengths.append(curr_length)
        curr_length = 0
lengths.append(curr_length)
print(max(lengths))
