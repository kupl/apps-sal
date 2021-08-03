v = input()
n = int(input())
q, s = [], [0 for i in range(-1, len(v))]
sol = ''

for i in range(1, len(v)):
    s[i] = s[i - 1]
    if v[i] == v[i - 1]:
        s[i] += 1

for i in range(0, n):
    x = tuple(map(int, input().split()))
    sol += str(s[x[1] - 1] - s[x[0] - 1]) + '\n'
print(sol)
