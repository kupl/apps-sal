N, K = list(map(int, input().split()))
Ps = list(map(int, input().split()))

ruisekiwa = [0]

for P in Ps:
    ruisekiwa.append(P + ruisekiwa[-1])

# print(ruisekiwa)
ans = 0
for i in range(N - K + 1):
    ans = max(ans, (ruisekiwa[i + K] - ruisekiwa[i] + K) / 2)
#    print(ans)
print(ans)
