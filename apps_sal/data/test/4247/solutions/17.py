n = int(input())
list_p = [int(i) for i in input().split()]
count = 0
for i in range(1, n - 1):
    if min(list_p[i - 1], list_p[i], list_p[i + 1]) != list_p[i] and \
            max(list_p[i - 1], list_p[i], list_p[i + 1]) != list_p[i]:
        count += 1
print(count)
