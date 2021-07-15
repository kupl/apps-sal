n = int(input())
s = str(input())

blocks = 0
current_size = 0
sizes = []

last = ""
for i in range(n):
    if i == 0 and s[i] == "B":
        blocks += 1
        current_size += 1
    else:
        if s[i] == "B":
            if last == "B":
                current_size += 1
            else:
                blocks += 1
                current_size = 1
        else:
            if last == "B":
                sizes.append(current_size)
    last = s[i]

if len(sizes) != blocks:
    sizes.append(current_size)

print(blocks)
if blocks != 0:
    print(*sizes)
