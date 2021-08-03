n = int(input())
lst = list(map(int, input().split()))
for i in range(len(lst) - 1, 0, -1):
    if lst[i] != lst[i - 1]:
        pos = i + 1
        break
    if i == 1:
        pos = 1
print(pos)
