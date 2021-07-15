import sys
n = int(input())
S = input()
for l in range(n):
    if S[l] == "*":
        d = 1
        while l + 4 * d < n:
            if S[l + d] == S[l + 2 * d] == S[l + 3 * d] == S[l + 4 * d] == "*":
                print("yes")
                return
            d += 1
print("no")



