from collections import defaultdict


def main():
    (n, k) = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    s = []
    ord = [-1] * (n + 1)
    u = 1
    while ord[u] == -1:
        ord[u] = len(s)
        s.append(u)
        u = a[u - 1]
    l = len(s) - ord[u]
    if k < ord[u]:
        print(s[k])
    else:
        print(s[(k - ord[u]) % l + ord[u]])


'\ndef main():\n    n, k = map(int, input().split(" "))\n    a = list(map(lambda i: int(i)-1, input().split(" ")))\n    s = [0]\n    d = defaultdict(lambda:0)\n    x = a[0]\n    for i in range(n):\n        s.append(x)\n        x = a[x]\n\n    bb=None\n    for i in range(n):\n        d[s[i]] += 1\n        if d[s[i]] ==2:\n            bb=s[i]\n            break\n\n    cc = s.index(bb)\n    s[cc]=-1\n    dd = s.index(bb)\n    loop_len = dd-cc\n    s[cc]=s[dd]\n        \n    if bb ==None or k < cc:\n        print(s[k]+1)\n    else:\n        y = (k-cc) % loop_len\n        print(s[y+cc]+1)\n'


def __starting_point():
    main()


__starting_point()
