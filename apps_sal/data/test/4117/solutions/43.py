n = int(input())
L = list(map(int, input().split()))
count = 0
for a in range(n - 2):
    for b in range(a + 1, n - 1):
        for c in range(b + 1, n):
            if L[a] + L[b] > L[c] and L[b] + L[c] > L[a] and (L[c] + L[a] > L[b]):
                if L[a] != L[b] and L[b] != L[c] and (L[c] != L[a]):
                    count += 1
print(count)
