n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print(arr[0])
else:
    brr = [abs(i) for i in arr]
    fl = False
    for i in range(n - 1):
        if arr[i] * arr[i + 1] < 0:
            fl = True
    if not fl:
        print(sum(brr) - 2 * min(brr))
    else:
        print(sum(brr))
'\nn = int(input())\narra = list(map(int, input().split()))\narrb = list(map(int, input().split()))\narra.sort()\narrb.sort()\na = 0\nb = 0\nfor i in range(2 * n):\n    if i % 2 == 0:\n        if len(arra) == 0:\n            arrb.pop()\n        elif len(arrb) == 0 or arra[-1] >= arrb[-1]:\n            a += arra[-1]\n            arra.pop()\n        else:\n            arrb.pop()\n    else:\n        if len(arrb) == 0:\n            arra.pop()\n        elif len(arra) == 0 or arrb[-1] >= arra[-1]:\n            b += arrb[-1]\n            arrb.pop()\n        else:\n            arra.pop()\nprint(a - b)\n'
"\nn = int(input())\nif n == 1 or n == 2:\n    print('No')\nelse: #if n % 2 == 1:\n    print('Yes')\n    print((n + 1) // 2, end = ' ')\n    for i in range(1, n + 1, 2):\n        print(i, end = ' ')\n    print()\n    print(n // 2, end = ' ')\n    for i in range(2, n + 1, 2):\n        print(i, end = ' ')\n"
'\nn, k = map(int, input().split())\ns = input()\nd = [0 for _ in range(k)]\nfor i in s:\n    d[ord(i) - ord(\'A\')] += 1\n#al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"\n#for i in \nprint(min(d) * k)\n'
