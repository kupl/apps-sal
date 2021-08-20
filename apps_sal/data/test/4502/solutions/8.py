n = int(input())
a = list(map(int, input().split()))
'\nb = []\n\nfront = False\nfor i in a:\n    if front:\n        b.insert(0, i)\n        front = False\n    else:\n        b.append(i)\n        front = True\n\n\n\n\nif front:\n    b.reverse()\n\n\nb = list(map(str, b))\nb = " ".join(b)\nprint(b)\n'
first = a[0:n:2]
last = a[1:n:2]
last = last[::-1]
answer = last + first
if n % 2 != 0:
    answer = answer[::-1]
print(*answer, sep=' ')
