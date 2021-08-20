(A, B) = map(int, input().split())
ans = 0
for i in range(A, B + 1):
    for j in range(len(str(i))):
        zen = j
        kou = len(str(i)) - 1 - j
        if zen >= kou:
            ans += 1
            break
        if str(i)[zen] != str(i)[kou]:
            break
print(ans)
