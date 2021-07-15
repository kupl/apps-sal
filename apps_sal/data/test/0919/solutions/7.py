n, k = list(map(int, input().split()))
a = [0] * 26
inn = input()
for i in inn:
    a[ord(i) - ord('a')] += 1
ans = 0
i = 0
anss = 0
while i < 26:
    if (a[i]):
        ans += 1
        anss += i + 1
        i += 1
    
    i += 1
    if (ans == k):
        break
    
if ans < k:
    print(-1)
else:
    print(anss)
