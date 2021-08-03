a, b = input().split(":")

ans = 0
while a[1] != b[0] or a[0] != b[1]:
    ans += 1
    x = 0
    if b == "59":
        x += 1
    b = str((int(b) + 1) % 60).zfill(2)
    a = str((int(a) + x) % 24).zfill(2)
print(ans)
