names = ["Danil", "Olya", "Slava", "Ann", "Nikita"]

A = input()

val = 0

for name in names:
    val += A.count(name)

if val == 1:
    print("YES")
else:
    print("NO")
