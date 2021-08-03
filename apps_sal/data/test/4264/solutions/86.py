N = int(input())
Ans = 0

for i in range(1, N + 1):
    if len(str(i)) % 2 == 1:
        Ans += 1

print(Ans)
