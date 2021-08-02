def solve(s):
    s = "".join(sorted(s))
    if s == s[::-1]:
        return -1
    else:
        return s


t = int(input())
for _ in range(t):
    x = input()
    print(solve(x))
