a, b, c = list(map(int, input().split()))

aa = a
s = a % b
data = []

while True:
    aa += a
    data.append(aa % b)
    if aa % b == s:
        break

data.sort()

if a % b == 0:
    print("NO")
elif c % data[1] != 0:
    print("NO")
else:
    print("YES")
