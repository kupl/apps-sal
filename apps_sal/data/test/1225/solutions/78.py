H = int(input())
ans = 1
while H:
    H //= 2
    ans *= 2
print(ans-1)
