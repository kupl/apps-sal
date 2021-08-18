
n = int(input())

l = list(map(int, input().split(" ")))


m = max(l)

i = 1

while (i * i <= m):
    if(m % i == 0):
        if(len(l) > 0 and (i in l)):
            l.remove(i)
        if(len(l) > 0 and ((m // i) in l) and (i != (m // i))):
            l.remove(m // i)
    i += 1

print(m, max(l))
