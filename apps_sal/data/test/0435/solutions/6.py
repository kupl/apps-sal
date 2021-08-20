def solve(n, k, l):
    ki = i = s = 0
    po = 1
    for j in range(n):
        s += l[j] == 0
        while s > k:
            s -= l[i] == 0
            i += 1
        if j - i > ki - po:
            (po, ki) = (i, j)
    return ki - po + 1


(n, k) = map(int, input().split())
s = input()
(list1, list2) = ([], [])
for i in range(n):
    if s[i] == 'a':
        list1.append(1)
        list2.append(0)
    else:
        list1.append(0)
        list2.append(1)
print(max(solve(n, k, list1), solve(n, k, list2)))
