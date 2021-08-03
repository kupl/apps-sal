n = int(input())
s = input()
ans = 0
p = None
for letter in s:
    if letter != p:
        p = letter
        ans += 1
print(ans)
