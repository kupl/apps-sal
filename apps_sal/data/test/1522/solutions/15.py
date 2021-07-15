n = int(input())
b = input()
a = set()
d = dict()
count = 0
for i in range(2 * n - 2):
    if i % 2 == 0:
        if b[i] not in a:
            a.add(b[i])
            d[b[i]] = 1
        else:
            d[b[i]] += 1
    else:
        if b[i].lower() in a:
            d[b[i].lower()] -= 1
            if d[b[i].lower()] == 0:
                a.remove(b[i].lower())
        else:
            count += 1    
print(count)
