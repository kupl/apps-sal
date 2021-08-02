n, m, k = [int(x) for x in input().split()]
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

sum_score = 0
sum_remove = 0
for i in range(m):
    num_of_ones = [0]
    num1 = 0
    for j in range(n):
        if matrix[j][i] == 1:
            num1 += 1
        num_of_ones.append(num1)

    max_score = 0
    num_remove = 0
    for j in range(0, n - k + 1):
        num_of_ones_in_range = num_of_ones[j + k] - num_of_ones[j]
        if num_of_ones_in_range > max_score:
            max_score = num_of_ones_in_range
            num_remove = num_of_ones[j]
    sum_score += max_score
    sum_remove += num_remove

print(sum_score, sum_remove)
