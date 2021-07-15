n = input()
n = int(n)
a = input()
a = a.split()
a = [int(i) for i in a]
a.sort()
answer = [0]*n
even = 0
odd = 0
for i, value in enumerate(a):
    if i % 2 == 0:
        answer[even] = str(value)
        even = even + 1
    else:
        answer[n-1-odd] = str(value)
        odd = odd + 1
print(" ".join(answer))
