n = int(input())
l = list(map(int, input().split()))
len_l = len(l)

ans = 0

for i in range(len_l - 2):
    for j in range(i + 1, len_l - 1):
        for k in range(j + 1, len_l):
            if l[i] != l[j] and l[i] != l[k] and l[j] != l[k]:
                if l[i] + l[j] > l[k] and l[i] + l[k] > l[j] and l[j] + l[k] > l[i]:
                    ans += 1

print(ans)
