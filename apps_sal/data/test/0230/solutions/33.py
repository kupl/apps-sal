N = int(input())
S = input()
l = 0
r = N
while l + 1 < r:
    x = (l + r) // 2
    first_loc = {}
    possible = False
    for i in range(N - x + 1):
        sub = S[i:i + x]
        if sub in first_loc:
            if first_loc[sub] <= i - x:
                possible = True
                break
        else:
            first_loc[sub] = i
    if possible:
        l = x
    else:
        r = x
print(l)
