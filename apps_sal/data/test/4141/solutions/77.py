input()
a = [a for a in map(int, input().split())if a % 2 == 0]
r = "DENIED"
for i in a:
    if i % 3 and i % 5:
        break
else:
    r = "APPROVED"
print(r)
