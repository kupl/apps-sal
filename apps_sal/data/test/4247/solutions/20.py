permutation_number = int(input())
permutation = list(map(int, input().split()))
conditional_permutation = 0
for i in range(permutation_number - 2):
    if permutation[i] < permutation[i + 1] < permutation[i + 2] or permutation[i] > permutation[i + 1] > permutation[i + 2]:
        conditional_permutation += 1
print(conditional_permutation)
