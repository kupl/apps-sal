s = input()
k = int(input())
substring = set([])
for i in range(min(len(s), 5)):
    for j in range(0, len(s)-i):
        substring.add(s[j:i+j+1])
ans = list(substring)
ans.sort()
print(ans[k-1])
