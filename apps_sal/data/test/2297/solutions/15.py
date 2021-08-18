
for _ in range(int(input())):
    i, j = map(int, input().split())
    i -= 1
    print(j // 2 * (j // 2 + 1) - i // 2 * (i // 2 + 1)
          - (((j -  j // 2) * (j - j // 2)) - ((i - i // 2) * (i - i // 2))))
