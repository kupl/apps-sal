s = input()
t = input()
fp = [-1]
tp = 0
for i in range(len(s)):
    if s[i] == t[tp]:
        fp.append(i)
        tp += 1
        if tp == len(t):
            break
lp = [len(s)]
tp = len(t) - 1
for i in range(len(s) - 1, -1, -1):
    if s[i] == t[tp]:
        lp.append(i)
        tp -= 1
        if tp == -1:
            break
lp.reverse()
print(max([l - f for (l, f) in zip(lp, fp)]) - 1)
