k = int(input())
kkk = [0] * k
kkk[0] = 7 % k
ans = -1
for i in range(1, k):
    kkk[i] = (kkk[i - 1] * 10 + 7) % k
for j in range(k):
    if kkk[j] == 0:
        ans = j + 1
        break
print(ans)
