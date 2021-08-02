import re
Sd = input()
T = input()
Sdls = list(Sd)
Sdls.reverse()
Sdre = ''.join(Sdls)
Tls = list(T)
Tls.reverse()
Tre = ''.join(Tls)
st = -1
for i in range(0, len(Sd) - len(T) + 1):
    f = 1
    for j in range(len(T)):
        if Tre[j] == Sdre[i + j] or Sdre[i + j] == '?':
            continue
        else:
            f = 0
            break
    if f == 1:
        st = i
        break
if st == -1:
    print('UNRESTORABLE')
else:
    Sdrels = list(Sdre)
    for j in range(len(T)):
        Sdrels[j + st] = Tre[j]
    for j in range(len(Sd)):
        if Sdrels[j] == '?':
            Sdrels[j] = 'a'
    ans = ''.join(reversed(Sdrels))
    print(ans)
