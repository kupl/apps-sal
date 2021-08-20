prime = 998244353
n = int(input())
arr = list(input().split())
count = [0 for i in range(11)]
count2 = [0 for i in range(11)]
for i in arr:
    count[len(i)] += 1
for i in range(1, 11):
    count2[i] = count2[i - 1] + count[i]
ans = 0
for i in arr:
    place = 1
    k = 1
    for j in range(len(i) - 1, -1, -1):
        ans = (ans + (count2[10] - count2[k - 1]) * place * int(i[j])) % prime
        ans = (ans + (count2[10] - count2[k - 1]) * place * int(i[j]) * 10) % prime
        for l in range(1, k):
            ans = (ans + 2 * count[l] * pow(10, l + k - 1) * int(i[j])) % prime
        place = place * 100
        k += 1
print(ans)
