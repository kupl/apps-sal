n = int(input()) 
f = list(map(int,input().split()))
t = sum(f)

n += 1
c_pos = t % n
x = 0

for i in range(1,6):
    if (c_pos + i) % n != 1 :
        x += 1
print(x)

