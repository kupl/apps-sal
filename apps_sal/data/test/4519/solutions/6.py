import sys
q = int(input())
for qi in range(q):
    (n, k) = list(map(int, input().split()))
    s = list(input())
    s = [0 if x == '0' else 1 for x in s]
    zc = oc = 0
    found = False
    for i in range(len(s)):
        if s[i] == 1:
            oc += 1
        elif oc <= k:
            k -= oc
            zc += 1
        else:
            res = [0] * zc
            res += [1] * (oc - k)
            res += [0]
            res += [1] * k
            res += s[i + 1:]
            print(''.join((str(x) for x in res)))
            found = True
            break
    if not found:
        res = [0] * zc
        res += [1] * oc
        print(''.join((str(x) for x in res)))
