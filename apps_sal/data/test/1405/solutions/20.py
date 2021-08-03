from sys import stdin, stdout


def fin(): return stdin.readline().strip()
def fout(x): stdout.write(str(x) + '\n')


def m_add(mp, val):
    mp[val] = mp.get(val, 0) + 1


def m_remove(mp, val):
    if mp[val] == 1:
        mp.pop(val)
    else:
        mp[val] -= 1


n, arr, mp, res = int(fin()), list(map(int, fin().split())), {}, 0
for i in arr:
    m_add(mp, i)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        cnt, a, b = 2, arr[i], arr[j]

        if a == 0 and b == 0:
            res = max(res, mp[0])
            continue

        m_remove(mp, a)
        m_remove(mp, b)

        while a + b in mp:
            m_remove(mp, a + b)
            a, b = b, a + b
            cnt += 1

        res = max(res, cnt)
        while a != arr[i] or b != arr[j]:
            a, b = b - a, a
            m_add(mp, a + b)

        m_add(mp, a)
        m_add(mp, b)
print(res)
