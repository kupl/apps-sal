n = int(input())
x = [int(i) for i in input().split()]
ave = sum(x) // n
ansl = 0
ansr = 0

for i in x:
    ansl += pow(i - ave, 2)
    ansr += pow(i - ave - 1, 2)

print(min([ansl, ansr]))
