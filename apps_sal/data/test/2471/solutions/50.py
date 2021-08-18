H, W, N = map(int, input().split())
li = []
for i in range(N):
    li.append(tuple(map(int, input().split())))
t = tuple(li)
st = set(t)

Js = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for a, b in t:
    if a > H - 2 or b > W - 2:
        pass
    else:
        t_p1 = ((a, b), (a, b + 1), (a, b + 2),
                (a + 1, b), (a + 1, b + 1), (a + 1, b + 2),
                (a + 2, b), (a + 2, b + 1), (a + 2, b + 2))
        s1 = st & set(t_p1)
        ls1 = len(s1)
        Js[ls1] += 1

    if a > H - 2 or b > W - 1 or b < 2:
        pass
    else:
        t_p2 = ((a, b - 1), (a, b), (a, b + 1),
                (a + 1, b - 1), (a + 1, b), (a + 1, b + 1),
                (a + 2, b - 1), (a + 2, b), (a + 2, b + 1))
        s2 = st & set(t_p2)
        ls2 = len(s2)
        Js[ls2] += 1

    if a > H - 2 or b < 3:
        pass
    else:
        t_p3 = ((a, b - 2), (a, b - 1), (a, b),
                (a + 1, b - 2), (a + 1, b - 1), (a + 1, b),
                (a + 2, b - 2), (a + 2, b - 1), (a + 2, b))
        s3 = st & set(t_p3)
        ls3 = len(s3)
        Js[ls3] += 1

    if a > H - 1 or a < 2 or b > W - 2:
        pass
    else:
        t_p4 = ((a - 1, b), (a - 1, b + 1), (a - 1, b + 2),
                (a, b), (a, b + 1), (a, b + 2),
                (a + 1, b), (a + 1, b + 1), (a + 1, b + 2))
        s4 = st & set(t_p4)
        ls4 = len(s4)
        Js[ls4] += 1

    if a > H - 1 or a < 2 or b > W - 1 or b < 2:
        pass
    else:
        t_p5 = ((a - 1, b - 1), (a - 1, b), (a - 1, b + 1),
                (a, b - 1), (a, b), (a, b + 1),
                (a + 1, b - 1), (a + 1, b), (a + 1, b + 1))
        s5 = st & set(t_p5)
        ls5 = len(s5)
        Js[ls5] += 1

    if a > H - 1 or a < 2 or b < 3:
        pass
    else:
        t_p6 = ((a - 1, b - 2), (a - 1, b - 1), (a - 1, b),
                (a, b - 2), (a, b - 1), (a, b),
                (a + 1, b - 2), (a + 1, b - 1), (a + 1, b))
        s6 = st & set(t_p6)
        ls6 = len(s6)
        Js[ls6] += 1

    if a < 3 or b > W - 2:
        pass
    else:
        t_p7 = ((a - 2, b), (a - 2, b + 1), (a - 2, b + 2),
                (a - 1, b), (a - 1, b + 1), (a - 1, b + 2),
                (a, b), (a, b + 1), (a, b + 2))
        s7 = st & set(t_p7)
        ls7 = len(s7)
        Js[ls7] += 1

    if a < 3 or b > W - 1 or b < 2:
        pass
    else:
        t_p8 = ((a - 2, b - 1), (a - 2, b), (a - 2, b + 1),
                (a - 1, b - 1), (a - 1, b), (a - 1, b + 1),
                (a, b - 1), (a, b), (a, b + 1))
        s8 = st & set(t_p8)
        ls8 = len(s8)
        Js[ls8] += 1

    if a < 3 or b < 3:
        pass
    else:
        t_p9 = ((a - 2, b - 2), (a - 2, b - 1), (a - 2, b),
                (a - 1, b - 2), (a - 1, b - 1), (a - 1, b),
                (a, b - 2), (a, b - 1), (a, b))
        s9 = st & set(t_p9)
        ls9 = len(s9)
        Js[ls9] += 1

for i in range(1, 10):
    Js[i] = Js[i] // i

all = (H - 2) * (W - 2)
Js[0] = all - sum(Js)

for i in range(10):
    print(Js[i])
