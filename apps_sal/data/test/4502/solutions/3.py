n = int(input())
a = list(map(str, input().split()))
b = []
'\nb = [str(a[0])]\nif (n == 1):\n    print(a[0])\n    return\n\na = a[1:]\n\nfor i in a:\n    b.append(str(i))\n    b.reverse()\n'
'\nloop = int(n / 2)\nloop_rest = n - loop\n\nfor i in range(loop):\n    tar_index = (n - 1) - 2 * i\n    tar = a[tar_index]\n\n    b.append(str(tar))\n\n\nif (n % 2 == 0):\n    tar_index = 0\nelse:\n    tar_index = 1\n\nfor i in range(loop_rest):\n    b.append(str(a[tar_index]))\n    tar_index += 2\n'
if n % 2 == 1:
    print(' '.join(a[0::2][::-1] + a[1::2]))
else:
    print(' '.join(a[1::2][::-1] + a[0::2]))
