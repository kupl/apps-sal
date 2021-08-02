N = int(input())

counter = 0

for i in range(105, N + 1, 2):
    div_counter = 0
    j = 1
    while j <= i:
        if (i % j) == 0:
            div_counter += 1
        j += 1

    if div_counter == 8:
        counter += 1


print(counter)
