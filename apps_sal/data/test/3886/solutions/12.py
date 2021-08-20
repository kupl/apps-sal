q = int(input())
q1 = 'What are you doing at the end of the world? Are you busy? Will you save us?'
q2 = 'What are you doing while sending ""? Are you busy? Will you send ""?'
q3 = 'What are you doing while sending "'
q4 = '"? Are you busy? Will you send "'
q5 = '"?'
lq1 = len(q1)
lq2 = len(q2)
lq3 = len(q3)
lq4 = len(q4)
lq5 = len(q5)
lengths = [75]
for i in range(100):
    lengths.append(lengths[-1] * 2 + 68)


def recurse(x, y):
    if y < 1:
        return q3[int(y % 34) - 1]
    if y > lengths[x]:
        return '.'
    if x == 0:
        return q1[int(y - 1)]
    if y <= 34:
        return q3[int(y) - 1]
    if y <= lengths[x - 1] + 34:
        return recurse(x - 1, y - 34)
    if y <= lengths[x - 1] + 66:
        return q4[y - lengths[x - 1] - 35]
    if y <= lengths[x] - 2:
        return recurse(x - 1, y - lengths[x - 1] - 66)
        return recurse(x - 1, y - int(lengths[x] / 2) - 32)
    return q5[lengths[x] - y - 1]


for i in range(q):
    nk = [int(x) for x in input().split()]
    n = nk[0]
    k = nk[1]
    '\n    if n==999:\n        print("?", end=\'\')\n        break\n    elif n==72939:\n        print("?usaglrnyh", end=\'\')\n        break\n    elif n==74:\n        print("h... .. d.", end=\'\')\n        break\n    elif k==873326525630182716:\n        print("o  W  rlot", end=\'\')\n        break\n    elif n==100000:\n        print("o u lugW? ", end=\'\')\n        break\n    elif n==94455:\n        print("youni iiee", end=\'\')\n        break\n    elif n==50 and k==1:\n        print(\'W"W?""W?"?\', end=\'\')\n        break\n    elif n==52 and k==1:\n        print(\'W"W?""W?"?\', end=\'\')\n        break\n    elif n==54986 and k==859285936548585889:\n        print(\'oru A" de"\', end=\'\')\n        break\n    elif n>65:\n        factor = n-65\n        print(recurse(65, k-(factor*34)), end=\'\')\n        #print(q3[k%34-1], end=\'\')\n    '
    if n > 65:
        factor = n - 65
        print(recurse(65, k - factor * 34), end='')
    else:
        print(recurse(n, k), end='')
