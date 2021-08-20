s = int(input())
for i in range(2, s + 1):
    if s % i == 0:
        print(str(i), str(s // i), sep='')
        break
