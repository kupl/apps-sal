S = input()
for i in range(3, 0, -1):
    if 'R' * i in S:
        print(i)
        break
else:
    print(0)
