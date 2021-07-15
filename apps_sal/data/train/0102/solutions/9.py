for _ in range(int(input())):
    limit = int(input())
    count = 0
    for numb in range(1, 10):
        i = 1
        while int(str(numb) * i) <= limit:
            count += 1
            i += 1
    print(count)

