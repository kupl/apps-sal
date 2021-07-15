a, b = map(int, input().split())
s = input()
letters = {}
for x in s:
    if not x in letters:
        letters[x] = 0
    letters[x] += 1
for x in letters.values():
    if x > b:
        print("NO")
        break
else:
    print("YES")
