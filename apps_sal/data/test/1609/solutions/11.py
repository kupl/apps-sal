n = int(input())
things_numbers = list(map(int, input().split()))
things_numbers_set = set(things_numbers)
is_not_free = set()
j = 1
for i in range(0, n):
    if things_numbers[i] not in is_not_free and things_numbers[i] <= n:
        is_not_free.add(things_numbers[i])
    else:
        while j in things_numbers_set:
            j += 1
        things_numbers[i] = j
        j += 1
print(*things_numbers)
