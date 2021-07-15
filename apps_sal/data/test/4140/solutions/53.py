w = list(input())
ans = 0
for i in range(len(w)-1):
    if w[i] == w[i+1]:
        if w[i] == "0":
            w[i+1] = "1"
        else:
            w[i+1] = "0"
        ans += 1
print(ans)
