def pgcd(a, b):
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b, r)


n, e = map(int, input().split())
events = list(map(int, input().split()))
settings = list(map(int, input().split()))
r = -1
for k in range(0, len(events) - 1):
    if(r == -1):
        r = events[k + 1] - events[k]
    else:
        r = pgcd(r, events[k + 1] - events[k])
ok = 0
for k in range(len(settings)):
    if(r % settings[k] == 0):
        print("YES")
        print(events[0], k + 1)
        ok = 1
        break
if(not ok):
    print("NO")
