bell = [a, b, c] = list(map(int, input().split(" ")))

print(sorted(bell).pop(0) +
      sorted(bell).pop(1))
