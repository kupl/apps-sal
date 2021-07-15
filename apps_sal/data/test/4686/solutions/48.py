l = input()

for i in l:
    if l.count(i) % 2 == 1:
        print("No")
        return
print("Yes")
