s = input()
sm = 0
a = ["Danil", "Olya", "Slava", "Ann", "Nikita"]
for i in a:
    sm += s.count(i)
if sm == 1:
    print("YES")
else:
    print("NO")
