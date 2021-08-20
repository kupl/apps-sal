n = int(input())
array = list(map(int, input().split()))


def is_even(k):
    return k % 2 == 0


new_array = []
for a in array:
    if a >= 0:
        new_array.append(-a - 1)
    else:
        new_array.append(a)
if not is_even(len(array)):
    positive = min(new_array)
    k = new_array.index(positive)
    new_array = new_array[:k] + [-new_array[k] - 1] + new_array[k + 1:]
print(' '.join(list(map(str, new_array))))
