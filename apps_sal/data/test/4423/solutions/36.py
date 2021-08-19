N = int(input())
book = []
for i in range(1, N + 1):
    (city, point) = input().split()
    point = int(point)
    book.append(((city, -point), i))
book.sort()
for info in book:
    print(info[1])
