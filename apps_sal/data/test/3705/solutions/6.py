n = int(input())
s = input()

for i in range(n, -1, -1):
    if s.count('8') < i:
        continue
    if (len(s) - i) // 10 < i:
        continue
    print(i)
    break
