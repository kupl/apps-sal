t = int(input())
for i in range(t):
    indexes = set()
    s = input()
    for j in range(len(s) - 2):
        if s[j:j + 3] == 'two':
            if j != len(s) - 3:
                if s[j + 3] != 'o':
                    indexes.add(j + 3)
                else:
                    indexes.add(j + 2)
            else:
                indexes.add(j + 2)
        elif s[j:j + 3] == 'one':
            if j == 0 or s[j - 1] != 'o':
                indexes.add(j + 1)
            else:
                indexes.add(j + 2)
    print(len(indexes))
    print(*indexes)
