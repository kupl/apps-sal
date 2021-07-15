n = int(input())
q = (n + 2 - 1) // 2
s = list(map(int, input().split()))
f = 0
for i in s:
    if(i > 0):
        q -= 1
    elif(i < 0):
        f += 1
if(q <= 0):
    print(1)
elif(f >= (n + 2 - 1) // 2):
    print(-1)
else:
    print(0)
