(n, x) = list(map(int, input().split()))
m = []
for _ in range(n):
    m.append(int(input()))
m.sort()


def main():
    for i in range(n):
        if sum(m[0:i + 1]) > x:
            print(i)
            return
    print(n)


if sum(m) > x:
    main()
else:
    print(n + (x - sum(m)) // m[0])
