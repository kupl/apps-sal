n = int(input())
s = [int(i) for i in input().split()]
u = ["a", "o", "i", "u", "e", "y"]
y = 1
for i in range(n):
    count = 0
    t = input()
    for j in t:
        if j in u:
            count += 1
    if count != s[i]:
        y = 0
if not y:
    print("NO")
else:
    print("YES")
