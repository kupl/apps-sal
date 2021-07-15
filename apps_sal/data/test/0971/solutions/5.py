from sys import stdin

n, b, d = (int(x) for x in stdin.readline().split())
a = list(int(x) for x in stdin.readline().split())

container = 0
result = 0

for orange in a:
    if orange > b:
        continue
    container += orange
    if container > d:
        result += 1
        container = 0

print(result)

