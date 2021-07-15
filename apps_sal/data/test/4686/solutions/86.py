w = input()
ans = "Yes"

for i in range(26):
    if w.count(chr(ord("a")+i)) % 2 == 1:
        ans = "No"
        break

print(ans)

