n = int(input())
nums = []
people = [True] * 2 * n
pairs = [-1] * 2 * n
for i in range(1, 2 * n):
    i_nums = list(map(int, input().split()))
    nums += list(zip(i_nums, [i] * i, range(i)))
nums.sort(key=lambda x: x[0], reverse=True)
for (num, i, j) in nums:
    if people[i] and people[j]:
        people[i] = people[j] = False
        pairs[i] = str(j + 1)
        pairs[j] = str(i + 1)
print(' '.join(pairs))
