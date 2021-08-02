K = int(input())

seven = [0] * K
seven[0] = 7 % K
for i in range(1, K):
    seven[i] = (10 * seven[i - 1] + 7) % K


for i in range(K):
    if seven[i] == 0:
        print(i + 1)
        return
print(-1)
