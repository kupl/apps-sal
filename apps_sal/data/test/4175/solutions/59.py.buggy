n = int(input())
seen = set()
tmp = ""
for _ in range(n):
    x = input()
    if not tmp:
        seen.add(x)
        tmp = x[-1]
        continue
    elif x[0] != tmp or x in seen:
        print("No")
        return
    else:
        seen.add(x)
        tmp = x[-1]
print("Yes")
