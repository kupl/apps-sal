


def main():
    a, b = list(map(int, input().split()))
    k = b // 2
    print(min(a - (a % b - k), a))



c = int(input())

for i in range(c):
    main()


