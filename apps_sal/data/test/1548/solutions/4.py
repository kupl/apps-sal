def mi():
    return list(map(int, input().split()))


'''
3
1 2 3
4
1 1 2 2
'''
n = int(input())
a = list(mi())

a.sort()
f, l = 0, 0
for i in range(n // 2):
    f += a[i]
    l += a[n - 1 - i]
if n % 2:
    if f > l:
        f += a[n // 2]
    else:
        l += a[n // 2]
print(f**2 + l**2)
