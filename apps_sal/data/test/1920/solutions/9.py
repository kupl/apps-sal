n = int(input())
boy = [0] * 1000
girl = [0] * 1000
for i in range(n):
    lst = list(input().split())
    lst[1] = int(lst[1])
    lst[2] = int(lst[2])
    for j in range(lst[1], lst[2] + 1):
        if lst[0] == 'M':
            boy[j] += 1
        else:
            girl[j] += 1
ans = -1
for i in range(1000):
    k = 2 * min(boy[i], girl[i])
    ans = max(ans, k)

print(ans)
