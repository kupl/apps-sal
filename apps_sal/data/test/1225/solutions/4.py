H = int(input())
cnt = 0
while H:
    H //= 2
    cnt = cnt * 2 + 1
print(cnt)
