def podstroki(s):
    return sorted(set(s[i: i1] for i in range(9) for i1 in range(i + 1, 10)), key=len)


res = {}
spisok = [podstroki(input()) for i in range(int(input()))]
for s in spisok:
    for podstr in s:
        if podstr in res:
            res[podstr] += 1
        else:
            res[podstr] = 1

for s in spisok:
    for podstr in s:
        if res[podstr] == 1:
            print(podstr)
            break
