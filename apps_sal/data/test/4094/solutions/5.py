ans = -1
a = 0
K = int(input())
if K % 2 == 0:
    ans = -1
elif K % 5 == 0:
    ans = -1
else:
    for i in range(0, K):
        a = (10 * a + 7) % K
        if a == 0:
            ans = i + 1
            break
print(ans)
