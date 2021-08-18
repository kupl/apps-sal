n = int(input())
s = input().strip()
for i in range(n):
    DP = [0] * n
    for j in range(n):
        if s[j] == "*":
            DP[j] = 1
            if j >= i and s[j - i] == '*':
                DP[j] += DP[j - i]
    if max(DP) >= 5:
        # print(i,max(DP))
        print("yes")
        return
print('no')
