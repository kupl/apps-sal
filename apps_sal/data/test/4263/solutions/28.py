X = ["A","C", "G", "T"]
S = input()
sum = 0
ans = 0
for i in S:
    if i in X:
        sum += 1
    else:
        sum = 0
    ans = max(sum, ans)
print(ans)
