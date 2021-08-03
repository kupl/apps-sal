n = int(input())
flowers = input().split()
odd = 0
ott = 0
for val in flowers:
    if int(val) % 2 == 0:
        odd += 1
    else:
        ott += 1

while ott > odd + 2:
    ott -= 2
    odd += 1

print(min(odd, ott))
