n, x = list(map(int, input().split()))
dis = list(map(int, input().split()))
dis.sort()
time = 0
for c in dis:
    time += c * x
    if(x != 1):
        x -= 1
print(time)
