from collections import Counter
s = Counter(input())
t = Counter(input())

ans = "Yes"
for x,y in zip(s.items(), t.items()):
    if x[1] != y[1]:
        ans = "No"
print(ans)
