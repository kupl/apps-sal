n = int(input())
w = list(map(int, input().split()))
difference_list = []
for i in range(n):
    score = abs(sum(w[:i]) - sum(w[i:]))
    difference_list.append(score)
print(min(difference_list))
