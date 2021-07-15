def check(p):
    for i in range(n - p):
        if a[i + p] - a[i] - 1 < d:
            return False
    
    return True


def binSearch(a, b):
    left, right = a - 1, b + 1

    while right - left > 1:
        mid = (left + right) // 2

        if check(mid):
            right = mid

        else:
            left = mid

    return right


n, m, d = map(int, input().split())
a = list(map(int, input().split()))

a_ind = {i: a[i] for i in range(n)}
a.sort()

b = binSearch(1, n)
ans = {el: 0 for el in a}

for i, el in enumerate(a, 1):
    ans[el] = (i - 1) % b + 1

print(b)
print(' '.join(map(str, [ans[a_ind[i]] for i in range(n)])))
