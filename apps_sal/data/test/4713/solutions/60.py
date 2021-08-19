n = int(input())
s = list(map(str, input()))
mx = 0
sm = 0
for char in s:
    if char == 'I':
        sm += 1
        mx = max(mx, sm)
    elif char == 'D':
        sm -= 1
    else:
        continue
print(mx)
