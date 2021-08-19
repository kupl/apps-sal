ss = input()
t = input()
ls = len(ss)
lt = len(t)
before = []
after = []
for i in range(ls - lt + 1):
    for j in range(lt):
        if ss[i + j] != '?':
            if ss[i + j] != t[j]:
                break
    else:
        before += [ss[:i] + t + ss[i + lt:]]
for k in before:
    after += [k.replace('?', 'a')]
if after:
    after = sorted(after)
    print(after[0])
else:
    print('UNRESTORABLE')
