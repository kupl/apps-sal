n = int(input())
students = [0] * 10010
mini = 4998
maxi = 5003
i = 5
j = 0
if n == 1:
      print(1)
      print(1)
elif n == 2:
    print(1)
    print(1)
elif n == 3:
    print(2)
    print(1,3)
else:
    students[4999] = 3
    students[5000] = 1
    students[5001] = 4
    students[5002] = 2
    while n >= i:
        if j == 0:
            j = 1
            students[mini] = i
            mini -= 1
        else:
            j = 0
            students[maxi] = i
            maxi += 1
        i += 1
    print(n)
    j = 0
    for z in range(2000,9000):
        if students[z] != 0 and j == 0:
            print(students[z],end=" ")
            

