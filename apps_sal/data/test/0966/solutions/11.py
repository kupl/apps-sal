3
y = int(input())
ans = y + 1
while True:
    if len(set(list(str(ans)))) == 4:
        break
    ans += 1
print(ans)
