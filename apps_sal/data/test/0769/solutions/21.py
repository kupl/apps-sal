a, b, c = list(map(int, input().split()))
pos = -1
for i in range(1, 309):
    if int((a * pow(10, i) // b)) % 10 == c:
        pos = i
        break
print(pos)

#128 7 0

