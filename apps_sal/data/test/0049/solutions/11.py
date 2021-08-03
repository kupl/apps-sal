

n = int(input())

x = 1

while n > (10**(len(str(x)) - 1) * 9 * len(str(x))):
    n -= 10**(len(str(x)) - 1) * 9 * len(str(x))

    x *= 10

t = len(str(x))
nadighe = False
while nadighe == False:
    qw = 1
    nadighe = True
    while n > (10**(len(str(qw)) - 1) * 9 * t):
        n -= 10**(len(str(qw)) - 1) * 9 * t
        nadighe = False
        qw *= 10
    x += qw - 1


while n > len(str(x)):
    n -= len(str(x))
    x += 1
for i in range(len(str(x))):
    if n != 0:
        s = str(x)[i]
        n -= 1
print(s)
