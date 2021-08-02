import math

n = input()
answer = len(n)
number = int(n)
for a in range(int(math.sqrt(int(n))), 1, -1):
    if number % a != 0:
        continue
    b = number // a
    answer = min(answer, max(len(str(a)), len(str(b))))
    break

print(answer)
