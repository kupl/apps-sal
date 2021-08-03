n = int(input())
after = {}
sets = [set(), set()]
for i in range(n):
    a, b = list(map(int, input().split()))
    sets[0].add(a)
    sets[1].add(b)
    after[a] = b
original_list = [0, (sets[0] - sets[1]).pop()]
for i in range(2, n + 2):
    original_list.append(after[original_list[i - 2]])
print(*original_list[1:n + 1])
