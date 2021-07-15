n, k = map(int, input().split())

for row in range(n):
        for col in range(n):
                if row == col:
                        print(k, end=' ')
                else:
                        print(0, end=' ')
        print()
