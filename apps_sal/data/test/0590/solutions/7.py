from collections import deque


def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for (i, x) in enumerate(a):
        d.setdefault(x, []).append(i)
    s = []
    c = {}
    for (k, v) in list(d.items()):
        s.extend(v)
        c[k] = len(v)
    s.sort()
    killed = set()
    ava = deque(sorted(frozenset(list(range(1, n + 1))) - frozenset(a)))
    ans = 0
    for i in s:
        v = a[i]
        if (c[v] == 1 or ava[0] > v) and (not v in killed):
            killed.add(v)
        else:
            a[i] = ava.popleft()
            ans += 1
        c[v] -= 1
    print(ans)
    print(' '.join(map(str, a)))


main()
