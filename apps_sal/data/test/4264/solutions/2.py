N = int(input())
Uneven_Numbers = []
for i in range(1, N + 1):
    count = len(str(i))
    if count % 2 != 0:
        Uneven_Numbers.append(i)
print(len(Uneven_Numbers))
