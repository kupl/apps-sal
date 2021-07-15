inp = input()

p, x, y = list(map(int, inp.split()))

Tshirt = []
s = x

while(s >= y):
    Tshirt = []
    ans = (s // 50) % 475
    for i in range(25):
        ans = (ans * 96 + 42) % 475
        Tshirt.append(ans + 26)

    if p in Tshirt:
        print(0)
        return
    s -= 50

hack = 0
while(not(p in Tshirt)):
    Tshirt = []
    ans = (x // 50) % 475
    for i in range(25):
        ans = (ans * 96 + 42) % 475
        Tshirt.append(ans + 26)
    x += 50
    hack += 1
    
print(hack // 2)

