input()
n = list(map(int, input().split()))
n = [ni - 1 if ni % 2 == 0 else ni for ni in n]
print(*n)
