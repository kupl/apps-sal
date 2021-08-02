inp = input().split()
n = int(inp[0])
m = int(inp[1])
z = int(inp[2])

for q in range(1, m + 1):
    if not (n * q) % m:
        break

lcm = n * q
print(z // (n * q))
