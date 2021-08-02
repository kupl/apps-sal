
road = input()
t = input()
cur = 0
for i in range(len(t)):
    if road[cur] == t[i]:
        cur += 1
print(cur + 1)
