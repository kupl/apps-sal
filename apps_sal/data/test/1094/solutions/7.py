n = int(input())
chat_list = []
names = set()
for i in range(n):
    name = input()
    if name not in names:
        names.add(name)
    chat_list.append(name)
x = len(names)
for i in chat_list[::-1]:
    if i in names:
        print(i)
        names.remove(i)
        x -= 1
        if x == 0:
            break
