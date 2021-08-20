(w, h, n) = map(int, input().split())
answ = set(range(w + 1))
ansh = set(range(w + 1))
for i in range(n):
    (x, y, a) = map(int, input().split())
    if a == 1:
        answ = answ & set(range(x, w + 1))
    elif a == 2:
        answ = answ & set(range(x + 1))
    elif a == 3:
        ansh = ansh & set(range(y, h + 1))
    elif a == 4:
        ansh = ansh & set(range(y + 1))
if len(answ) == 0 or len(ansh) == 0:
    print(0)
else:
    print((max(answ) - min(answ)) * (max(ansh) - min(ansh)))
