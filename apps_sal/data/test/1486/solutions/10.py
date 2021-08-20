n = int(input())
l = list(map(int, input().split(' ')))
for i in range(n):
    if i == 0:
        print(str(l[1] - l[0]) + ' ' + str(l[n - 1] - l[0]))
    elif i == n - 1:
        print(str(l[n - 1] - l[n - 2]) + ' ' + str(l[n - 1] - l[0]))
    else:
        print(str(min(l[i] - l[i - 1], l[i + 1] - l[i])) + ' ' + str(max(l[i] - l[0], l[n - 1] - l[i])))
