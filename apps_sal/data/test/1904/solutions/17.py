n = int(input())
word = list(input())
costs = list(map(int, input().rstrip().split()))
costlist = [0] * 4
for i in range(n):
    if word[i] == 'h':
        costlist[0] += costs[i]
    if word[i] == 'a':
        costlist[1] = min(costlist[0], costlist[1] + costs[i])
    if word[i] == 'r':
        costlist[2] = min(costlist[1], costlist[2] + costs[i])
    if word[i] == 'd':
        costlist[3] = min(costlist[2], costlist[3] + costs[i])
print(costlist[3])
