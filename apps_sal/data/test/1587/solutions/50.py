n = int(input())
C = list(input())
ans = 0
N = n - 1
for l in range(n):
    if C[l] == "W":
        for r in range(N, 0, -1):
            if r <= l:
                print(ans)
                return
            if C[r] == "R":
                # print(C)
                C[l] = "R"
                C[r] = "W"
                # print(C)
                # print("-----------------")
                ans += 1
                N = r - 1
                break
print(ans)
