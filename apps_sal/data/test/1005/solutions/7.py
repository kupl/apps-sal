t = int(input())
for z in range(t):
    n, k, d = map(int, input().split())
    arr = list(map(int, input().split()))
    m = dict([[i, 0] for i in range(k + 1)])
    emp = set()

    for i in range(d):
        x = arr[i]
        m[x] += 1
        emp.add(x)

    mn = len(emp)
    for i in range(d, n):
        x = arr[i - d]
        m[x] -= 1
        if m[x] == 0:
            emp.remove(x)

        x = arr[i]
        m[x] += 1
        emp.add(x)
        mn = min(mn, len(emp))
    print(mn)
