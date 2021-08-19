# B - Toll Gates

# N M X
N, M, X = list(map(int, input().split()))
my_list = list(map(int, input().split(maxsplit=M)))
count_start = 0
count_goal = 0

# 0へ行くパターン
for i in range(1, X):
    if i in my_list:
        count_start += 1

for i in range(X, N):
    if i in my_list:
        count_goal += 1

if count_start >= count_goal:
    answer = count_goal
else:
    answer = count_start

print(answer)
