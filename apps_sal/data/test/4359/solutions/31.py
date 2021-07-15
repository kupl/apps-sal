# ABC123
# Five Dishes
#B=A R=B G=C P=D T=E
Ryori = [input() for _ in range(5)]
O = []
t = 0
for i in Ryori:
    if int(i[-1]) == 0:
        x = Ryori.pop(Ryori.index(i))
        O.append(x)
Ryori = sorted(Ryori,key=lambda x: x[-1], reverse=True)

for i in range(len(Ryori)-1):
    for j in range(10):
        if (int(Ryori[i]) + j) % 10 == 0:
            t += int(Ryori[i]) + j
t += int(Ryori[-1])

for i in O:
    t += int(i)
print(t)

