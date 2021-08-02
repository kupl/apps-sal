a, b = map(int, input().split())
s = []
for i in range(a):
    s.append(input())
print("#" * (b + 2))
for i in range(a):
    print("#", end="")
    print(s[i], end="")
    print("#")
print("#" * (b + 2))
