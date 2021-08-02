K = int(input())
a = 7
flag = -1
for i in range(K):
    if a % K == 0:
        flag = i + 1
        break
    else:
        a = (10 * a + 7) % K
print(flag)
