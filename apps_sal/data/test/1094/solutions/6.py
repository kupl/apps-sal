message_count = int(input())
names = {}
last = 1
for i in range(message_count):
    name = input()
    names[name] = -i
sorted_names = sorted(names.keys(), key=lambda name: names[name])
[print(name) for name in sorted_names]
