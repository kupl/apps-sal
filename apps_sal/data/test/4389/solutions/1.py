tests = int(input())
for _ in range(tests):
    n = input()
    for i in range(len(n) // 2):
        print(n[2 * i], end='')
    print(n[-1])
