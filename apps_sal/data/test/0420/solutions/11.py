def check(i, j):
    nonlocal a
    while i < j:
        if a[i] != a[j]:
            return False
        i += 1
        j -= 1
    return True
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input().strip())
last = n
while last % 2 == 0:
    if check(0, last - 1):
        last //= 2
    else:
        break
print(last)
