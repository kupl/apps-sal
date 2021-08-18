import math
n = 3
k = 2

p = [1, 2, 3]
q = [1, 3, 2]

n, k = [int(x) for x in input().split(' ')]
p = [int(x) - 1 for x in input().split(' ')]
q = [int(x) - 1 for x in input().split(' ')]


group_ids = []


p_ids = set()
q_ids = set()
for i in range(n):
    if p[i] in q_ids:
        q_ids.remove(p[i])
    else:
        p_ids.add(p[i])

    if q[i] in p_ids:
        p_ids.remove(q[i])
    else:
        q_ids.add(q[i])

    if not bool(p_ids) and not bool(q_ids):
        group_ids.append(i)

if len(group_ids) < k:
    print('NO')
    return


def get_letter(_id):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet[min(_id, len(alphabet) - 1)]


print('YES')
result = [None] * n
l = 0
for i in range(len(group_ids)):
    r = group_ids[i]
    letter = get_letter(i)
    for it in range(l, r + 1):
        result[p[it]] = letter
    l = r + 1


print(''.join(result))
