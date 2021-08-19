for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = []
    y = []
    for i in range(n):
        if b[i] == 0:
            x.append(a[i])
        else:
            y.append(a[i])
    if len(x) == 0:
        if y == sorted(y):
            print('Yes')
        else:
            print('No')
    elif len(y) == 0:
        if x == sorted(x):
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')
        '\n        x.sort()\n        y.sort()\n        merged = []\n        i = 0\n        j = 0\n        for elem in b:\n            if elem == 0:\n                merged.append(x[i])\n                i += 1\n            else:\n                merged.append(y[j])\n                j += 1\n        if merged == sorted(merged):\n            print("Yes")\n        else:\n            print("No")\n'
