T = int(input())
for _ in range(T):
    (n, k) = map(int, input().split())
    if k % 3:
        if n % 3:
            print('Alice')
        else:
            print('Bob')
    else:
        loop = k + 1
        idx = n % loop
        if idx == k:
            print('Alice')
        elif idx % 3:
            print('Alice')
        else:
            print('Bob')
    '\n    sg = [0] * (n+3)\n    sg[1] = 1\n    sg[2] = 1\n    for i in range(3, n+1):\n        if sg[i-1] == 0:\n            sg[i] = 1\n        elif sg[i-2] == 0:\n            sg[i] = 1\n        elif i >= k and sg[i-k] == 0:\n            sg[i] = 1\n        else:\n            sg[i] = 0\n    if sg[n]:\n        print("Alice")\n    else:\n        print("Bob")\n    print(sg)\n    '
