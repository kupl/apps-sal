n = int(input())
p = list(map(int, input().split()))
l = input()
change = 0
max_change = 0
init_str = 0
for i in range(len(l)):
    if l[i] == 'A':
        change += p[i]
    else:
        change -= p[i]
        init_str += p[i]
    if max_change < change:
        max_change = change
max_change_back = 0
change = 0
for i in range(len(l) - 1, -1, -1):
    if l[i] == 'A':
        change += p[i]
    else:
        change -= p[i]
    if max_change_back < change:
        max_change_back = change
print(max(max_change_back, max_change) + init_str)

