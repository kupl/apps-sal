n = int(input())

a = [int(i) for i in input().split()]

av = sum(a) // len(a)

ans = 0

s = 0

for i in a:

    s += i - av

    ans += abs(s)

print(ans)
