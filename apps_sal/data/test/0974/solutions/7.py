n = int(input())
c = 1
sorts = 0
boxes = []

for _ in range(2 * n):
    s = input()
    if s[0] == 'a':
        boxes.append(int(s[4:]))
    else:
        if boxes:
            if boxes[-1] != c:
                boxes = []
                sorts += 1
            else:
                boxes.pop()
        c += 1
print(sorts)

