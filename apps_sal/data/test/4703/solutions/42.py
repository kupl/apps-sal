s = input()
total = 0
for i in range(len(s)):
    for j in range(len(s) - i):
        n = int(s[j:j + i + 1])
        if j == 0 or j == len(s) - i - 1:
            total += n * max([2 ** (len(s) - i - 2), 1])
        else:
            total += n * max([2 ** (len(s) - i - 3), 1])
print(total)
