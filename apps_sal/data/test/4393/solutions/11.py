n = int(input())
# m = list(map(int, input().split()))
s = input()
c = 1
sol = ''
i = 0
while i < n:
    sol += s[i]
    i += c
    c += 1
print(sol)
