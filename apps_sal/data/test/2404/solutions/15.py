a = int(input())
for i in range(2, a):
    if a % i == 0:
        print(str(int(i)) + str(a // i))
        break
