N = int(input())
lst = [111, 222, 333, 444, 555, 666, 777, 888, 999]
for i in lst:
    if N <= i:
        print(i)
        break
