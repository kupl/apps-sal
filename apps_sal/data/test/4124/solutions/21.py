a = input().strip()
b = input().strip()
ans = 0

ai = len(a) - 1
bi = len(b) - 1

while ai >= 0 and bi >= 0:
    if a[ai] == b[bi]:
        ans += 2
    else:
        break
    ai -= 1
    bi -= 1
print(len(a) + len(b) - ans)
