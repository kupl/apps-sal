import collections

n = int(input())
n_half = n//2
v = list(map(int, input().split()))
v_gusu = v[0::2]
v_odd = v[1::2]
ans = 0
c1 = collections.Counter(v)
c2 = collections.Counter(v_gusu)
c3 = collections.Counter(v_odd)

if c1.most_common()[0][1] == n:
    print(n_half)
    return

if c2.most_common()[0][0] == c3.most_common()[0][0]:
    print(min((n_half - c2.most_common()[1][1]) + (n_half - c3.most_common()[0][1]),(n_half - c2.most_common()[0][1]) + (n_half - c3.most_common()[1][1])))
    return
else:
    print((n_half - c2.most_common()[0][1]) + (n_half - c3.most_common()[0][1]))
    return
