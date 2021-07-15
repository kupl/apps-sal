a = int(input())
for i in range(1, 1000000):
    if i * i >= a:
        if i * (i - 1) >= a:
            print(2 * (i + i - 1));
        else:
            print(4 * i);
        break
