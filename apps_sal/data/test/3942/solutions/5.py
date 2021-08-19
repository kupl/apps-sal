a = input()
need = a.count('(') - a.count(')')
hashs = a.count('#')

last = need - (hashs - 1)
if last <= 0:
    print(-1)
    quit()
hashes = [i for i in range(len(a)) if a[i] == '#']

count = 0
for i in range(len(a)):
    if a[i] == '(':
        count += 1
    if a[i] == ')':
        count -= 1
    if a[i] == '#':
        if i == hashes[-1]:
            count -= last
        else:
            count -= 1
    if count < 0:
        print(-1)
        quit()

for i in range(hashs - 1):
    print(1)
print(last)
