a, b = map(int, input().split())
ans = []
for i in range(a, b + 1):
    c = [j for j in str(i)]
    if c[0] == c[-1] and c[1] == c[-2]:
        ans.append(i)
print(len(ans))
