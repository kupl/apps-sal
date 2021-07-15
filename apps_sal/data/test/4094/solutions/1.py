k = int(input())
aaa = [0] * k
aaa[0] = 7 % k
for i in range(1, k):
    aaa[i] = (aaa[i - 1] * 10 + 7) % k
ans = -1
for j in range(k):
    if aaa[j] == 0:
        ans = j + 1
        break
print(ans)

