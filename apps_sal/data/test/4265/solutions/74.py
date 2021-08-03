s = input()
t = input()

count = 0
for ss, tt in zip(s, t):
    if ss != tt:
        count += 1

print(count)
