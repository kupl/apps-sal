s = input()
size = 1
ans = 0
while len(s) > size:
    ans += (10 ** size - 10 ** (size - 1)) * size
    size += 1
s = int(s) - 10 ** (size - 1) + 1
ans += s * size
print(ans)
