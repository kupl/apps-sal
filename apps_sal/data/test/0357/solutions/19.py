s = input()
data = ["Danil", "Olya", "Slava", "Ann", "Nikita"]
count = 0
for i in range(5):
    if data[i] in s:
        count += s.count(data[i])
if count == 1:
    print("YES")
else:
    print("NO")
