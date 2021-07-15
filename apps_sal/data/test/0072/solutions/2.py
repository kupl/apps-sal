from collections import Counter;

n = int(input())

a = input()
b = input()
c = input()

fa = Counter(a);
fb = Counter(b);
fc = Counter(c);

la = min(fa.most_common(1)[0][1] + n, len(a))
lb = min(fb.most_common(1)[0][1] + n, len(a))
lc = min(fc.most_common(1)[0][1] + n, len(a))

if fa.most_common(1)[0][1] == len(a) and n == 1:
    la = len(a)-1

if fb.most_common(1)[0][1] == len(b) and n == 1:
    lb = len(b)-1

if fc.most_common(1)[0][1] == len(c) and n == 1:
    lc = len(c)-1



if la > max(lb, lc):
    print("Kuro")
elif lb > max(la, lc):
    print("Shiro")
elif lc > max(la, lb):
    print("Katie")
else:
    print("Draw")


