def main():
    n = int(input().strip()) + 1
    x = sum(map(int, input().strip().split())) % n
    return sum(((x + i) % n != 1 for i in range(1, 6)))


print(main())
