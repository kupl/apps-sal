n = int(input())
arra = list(map(int, input().split()))
arrb = list(map(int, input().split()))
arra.sort()
arrb.sort()
a = 0
b = 0
for i in range(2 * n):
    if i % 2 == 0:
        if len(arra) == 0:
            arrb.pop()
        elif len(arrb) == 0 or arra[-1] >= arrb[-1]:
            a += arra[-1]
            arra.pop()
        else:
            arrb.pop()
    elif len(arrb) == 0:
        arra.pop()
    elif len(arra) == 0 or arrb[-1] >= arra[-1]:
        b += arrb[-1]
        arrb.pop()
    else:
        arra.pop()
print(a - b)
"\nn = int(input())\nif n == 1 or n == 2:\n    print('No')\nelse: #if n % 2 == 1:\n    print('Yes')\n    print((n + 1) // 2, end = ' ')\n    for i in range(1, n + 1, 2):\n        print(i, end = ' ')\n    print()\n    print(n // 2, end = ' ')\n    for i in range(2, n + 1, 2):\n        print(i, end = ' ')\n"
'\nn, k = map(int, input().split())\ns = input()\nd = [0 for _ in range(k)]\nfor i in s:\n    d[ord(i) - ord(\'A\')] += 1\n#al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"\n#for i in \nprint(min(d) * k)\n'
