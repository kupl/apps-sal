Omoji = ['A', 'B', 'C']
Kmoji = ['a', 'b', 'c']
(n, k) = map(int, input().split())
s = str(input())
ans = ''
for i in range(n):
    if i == k - 1:
        for j in range(len(Omoji)):
            if s[i] == Omoji[j]:
                ans += Kmoji[j]
    else:
        ans += s[i]
print(ans)
