n, m, l = list(map(int, input().split()))
l += 1
hair = [1] * (n + 1)
other_end = [1] * (n + 1)
i = 1
j = 1
big = 1
res = 1
for a in map(int, input().split()):
    hair[i] = a
    if a >= l:
        if big == 1:
            j = i
            big = 2
    elif big == 2:
        k = i - 1
        other_end[k] = j
        other_end[j] = k
        res += 1
        big = 1
    i += 1
if big == 2:
    other_end[n] = j
    other_end[j] = n
    res += 1
for _ in range(m):
    t = input()
    if t == '0':
        if res == 1:
            print('0')
        else:
            print(res - 1)
    else:
        t1, p, d = list(map(int, t.split()))
        old = hair[p]
        hair[p] += d
        if hair[p] >= l > old:
            if p == 1 or hair[p - 1] < l:
                case_id = 1
            else:
                case_id = 2
            if p != n and hair[p + 1] >= l:
                case_id += 2
            if case_id == 1:
                other_end[p] = p
                res += 1
            elif case_id == 2:
                other_end[p] = other_end[p - 1]
                other_end[other_end[p]] = p
            elif case_id == 3:
                other_end[p] = other_end[p + 1]
                other_end[other_end[p]] = p
            else:
                left_end = other_end[p - 1]
                right_end = other_end[p + 1]
                other_end[left_end] = right_end
                other_end[right_end] = left_end
                res -= 1
