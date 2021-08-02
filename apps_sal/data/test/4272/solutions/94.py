n = int(input())
s = input()
count = 0
for i in range(3 + len(s) - 1):
    portion = s[i:i + 3]
    if 'ABC' == portion:
        count += 1

print(count)
