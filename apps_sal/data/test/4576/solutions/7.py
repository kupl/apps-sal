a = int(input())
b = int(input())
c = int(input())
x = int(input())
ans = 0
for aa in range(a + 1):
    for bb in range(b + 1):
        for cc in range(c + 1):
            if 500 * aa + 100 * bb + 50 * cc == x:
                ans += 1
print(ans)
