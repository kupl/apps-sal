from collections import Counter
input()
ans = [0, 0]
for (i, j) in list(Counter(list(map(int, input().split()))).items()):
    if j >= 4:
        ans.append(i)
    if j >= 2:
        ans.append(i)
ans.sort()
print(ans[-1] * ans[-2])
