def get_input_list():
    return list(map(int, input().split()))


def sort_(p):
    np = []
    for i in p:
        np.append([i[0], -i[1]])
    np.sort()
    return np


def distance(A, B):
    return abs(B[0] - A[0]) + abs(B[1] - A[1])


n = int(input())
p_ = []
for _ in range(n):
    p_.append(get_input_list())
d = {}
for i in p_:
    if (str(max(i))) in d:
        d[str(max(i))].append(i)
    else:
        d[str(max(i))] = [i]
l = [int(i) for i in d]
l.sort()
p1 = [0, 0]
p2 = [0, 0]
s1 = 0
s2 = 0
for i_ in l:
    i = str(i_)
    p = sort_(d[i])
    a1 = distance(p1, p[0])
    b1 = distance(p1, p[-1])
    a2 = distance(p2, p[0])
    b2 = distance(p2, p[-1])
    c = distance(p[0], p[-1])
    s1_ = s1
    s2_ = s2
    s1 = min(s2_ + a1, s1_ + a2) + c
    s2 = min(s2_ + b1, s1_ + b2) + c
    p1 = p[0]
    p2 = p[-1]
print(min(s1, s2))
