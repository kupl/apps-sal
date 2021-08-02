3

n = int(input())
s = input()

if n == 1:
    print("Yes")
    return

was = set()
for c in s:
    if c in was:
        print("Yes")
        return
    was.add(c)


print("No")
