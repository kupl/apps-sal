a = int(input())
for iter in range(a):
    b = input()
    if len(b) == 1:
        print(b)
        continue
    ans = (len(b) - 1) * 9
    counter = 0
    for iter in range(1, 10):
        if int(str(iter) * len(b)) <= int(b):
            counter += 1
    print(ans + counter)


