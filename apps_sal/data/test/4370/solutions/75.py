A, B = list(map(int, input().split()))

ans = str()
if (A <= 8) and (B <= 8):
    ans = "Yay!"
else:
    ans = ":("

print(ans)
