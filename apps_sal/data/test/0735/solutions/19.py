def issort(a):
    for k in range(len(a) - 1):
        if a[k] > a[k + 1]:
            return False
    return True


n = int(input())
a = list(map(int, input().split()))
(i, j) = (0, n - 1)
while i < n - 1 and a[i] < a[i + 1]:
    i += 1
while j > 0 and a[j] > a[j - 1]:
    j -= 1
if j == 0:
    print('yes')
    print(j + 1, j + 1)
elif issort(a[:i] + a[i:j + 1][::-1] + a[j + 1:]):
    print('yes')
    print(i + 1, j + 1)
else:
    print('no')
