(x, n) = map(int, input().split())
li_p = list(map(int, input().split()))
li_p.sort()
i = 0
while True:
    a = x - i
    b = x + i
    if not a in li_p:
        print(a)
        break
    elif a in li_p and (not b in li_p):
        print(b)
        break
    elif a in li_p and b in li_p:
        i += 1
