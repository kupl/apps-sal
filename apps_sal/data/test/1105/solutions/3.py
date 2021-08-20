def readln():
    return tuple(map(int, input().split()))


(n,) = readln()
max_pref = [-1] * 100001
flag = True
for _ in range(n):
    (x, k) = readln()
    flag &= max_pref[k] + 1 >= x
    max_pref[k] = max(max_pref[k], x)
print('YES' if flag else 'NO')
