N = int(input())
minimum = 100 
total = 0
for i in range(N):
    s = int(input())
    total += s 
    if s % 10 != 0:
        minimum = min(minimum,s)
if total % 10 != 0:
    print(total)
elif minimum == 100:
    print(0)
else:
    print(total - minimum)
