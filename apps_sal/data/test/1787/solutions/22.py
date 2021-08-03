def p(arr, n):
    ans = 1
    for i in range(0, n):
        ans = ans * (arr[i] + 1)
    return ans - 1


s = input()
a = []
k = 0
for i in s:
    if i == 'a':
        k += 1
    elif i == 'b':
        if k != 0:
            a.append(k)
        k = 0
if k != 0:
    a.append(k)
print(p(a, len(a)) % 1000000007)
