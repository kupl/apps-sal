def mi():
    return list(map(int, input().split()))


'''

'''

n = int(input())
a = list(mi())

a.sort()
s = 0
for i in range(n):
    if i % 2:
        continue
    s += abs(a[i + 1] - a[i])
print(s)
