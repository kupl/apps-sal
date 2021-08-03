N = int(input())
C = input()
R = C.count("R")
ans = 0

for r in range(R):
    if C[r] == "W":
        ans += 1

print(ans)
