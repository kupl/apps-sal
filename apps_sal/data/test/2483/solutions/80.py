(n, c, *stc) = list(map(int, open(0).read().split()))
stc = list(zip(stc[::3], stc[1::3], stc[2::3]))
stc.sort()
record = []
for (s, t, c) in stc:
    for (i, (rt, rc)) in enumerate(record):
        if s - 0.5 >= rt:
            record[i] = (t, c)
            break
        elif c == rc and s >= rt:
            record[i] = (t, c)
            break
    else:
        record.append((t, c))
    record.sort(reverse=True)
print(len(record))
