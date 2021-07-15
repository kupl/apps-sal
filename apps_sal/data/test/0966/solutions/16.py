n = int(input())
while True:
    n += 1
    c = set(str(n))
    if len(c) == len(str(n)):
        print(n)
        break


