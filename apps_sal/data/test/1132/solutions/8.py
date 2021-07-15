n, m = [int(k) for k in input().split()]
ans = 'bus topology'
dict = {}
count = 0
t = 0
if m >= n-1:
    for i in range(m):
        first, second = [int(k) for k in input().split()]
        if first not in dict:
            dict[first] = set()
            dict[first].add(second)
        else:
            if len(dict[first]) == 1:
                count += 1
            else: t += 1
            dict[first].add(second)
        if second not in dict:
            dict[second] = set()
            dict[second].add(first)
        else:
            if len(dict[second]) == 1:
                count += 1
            else: t += 1
            dict[second].add(first)
if count == n-2 and m == n-1:
    print('bus topology')
elif count == 1:
    print('star topology')
elif count == n and t == 0:
    print('ring topology')
else:
    print('unknown topology')

