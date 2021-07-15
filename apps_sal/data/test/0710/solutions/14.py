genome = "ACTG"


def diff(u):
    x = 0
    for i in range(4):
        a, b = ord(genome[i]) - ord('A'), ord(u[i]) - ord('A')
        x += min(abs(a - b),
                 abs(26 - max(a, b) + min(a, b)))
    return x


n = int(input())
s = input()

ans = float("inf")

for i in range(len(s) - 3):
    ans = min(ans, diff(s[i:i + 4]))

print(ans)

