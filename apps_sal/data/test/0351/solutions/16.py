n, k = map(int, input().split(' '))
problems = list(map(int, input().split(' ')))

problems.sort()
# easy = []

# for i in range(len(problems)):
# 	if problems[i] > k:
# 		problems = problems[i:]
# 		break

max_solved = k
problem_index = 0
n_has_to_solve = 0

while problem_index < n:
    if problems[problem_index] <= max_solved * 2:
        max_solved = max(max_solved, problems[problem_index])
        problem_index += 1
    else:
        max_solved *= 2
        n_has_to_solve += 1

print(n_has_to_solve)
