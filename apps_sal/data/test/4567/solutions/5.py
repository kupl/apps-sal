n = int(input())
s = sorted([int(input()) for _ in range(n)])

grade = 0 if sum(s) % 10 == 0 else (sum(s))

if grade == 0:
    for i in s:
        if i % 10 != 0:
            print((sum(s) - i))
            return

print(grade)
