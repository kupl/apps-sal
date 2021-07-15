X = int(input())
G = 100
after_year = 0

while X > G:
    G += G // 100
    after_year += 1

print(after_year)
