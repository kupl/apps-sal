N = int(input())

ans = "No"

for i in range(15):
    for j in range(26):
        if (i * 7 + j * 4) == N:
            ans = "Yes"
        else:
            pass

print(ans)
