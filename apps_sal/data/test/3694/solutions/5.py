n = int(input())
a = sorted(list(map(int, input().split())))
bal = 0
if a.count(0) > 1:
    print('cslnb')
    return
if n - len(set(a)) > 1:
    print('cslnb')
    return
if n - len(set(a)) == 1:
    for i in range(1, n):
        if a[i] == a[i - 1]:
            if a[i] - 1 in a:
                print('cslnb')
                return
            break
if n == 1:
    print('cslnb' if not a[0] % 2 else 'sjfnb')
    return

for i in range(n):
    bal += a[i] - i
print('sjfnb'if bal % 2 else 'cslnb')
