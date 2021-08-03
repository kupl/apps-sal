queries = []
for q in range(int(input())):
    old, new = input().split()
    done = False
    for elem in queries:
        if old == elem[-1]:
            elem.append(new)
            done = True
            break
    if not done:
        queries.append([old, new])
print(len(queries))
for elem in queries:
    print(elem[0], elem[-1])
