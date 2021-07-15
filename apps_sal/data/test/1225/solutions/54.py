H = int(input())
A = 0
ans = 0
for i in range(H):
    if 2**i <= H < 2**(i+1):
        A = 2**i
        break
    else:
        continue

for j in range(i+1):
    ans += 2**j

print(ans)

