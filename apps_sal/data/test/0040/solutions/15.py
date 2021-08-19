n = int(input())
L = []
ans = 'maybe'
for _ in range(n):
    (a, b) = list(map(int, input().split()))
    L.append((a, b))
    if a != b:
        ans = 'rated'
        break
L1 = L[:]
L1.sort(reverse=True)
for i in range(len(L)):
    if L[i] != L1[i] and ans != 'rated':
        ans = 'unrated'
        break
print(ans)
