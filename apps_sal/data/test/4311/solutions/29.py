a = int(input())

da = True
ap = [a]
count = 1
while da:
    if a % 2 == 0:
        a = a // 2
        ap.append(a)
    elif a % 2 == 1:
        a = 3 * a + 1
        ap.append(a)
    count += 1
    if len(set(ap)) < len(ap):
        print(count)
        da = False
