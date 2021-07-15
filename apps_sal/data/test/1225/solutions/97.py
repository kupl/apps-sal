# D
H = int(input())
cnt = 1
ans = 0

while True:
    if 2**cnt > H:
        cnt -= 1
        break
    elif 2**cnt == H:
        break
    else:
        cnt += 1

for c in range(cnt+1):
    ans += 2**c
print(ans)

