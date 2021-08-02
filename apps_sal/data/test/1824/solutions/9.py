n = input()
errors1 = sorted(list(map(int, input().split())), reverse=True)
errors2 = sorted(list(map(int, input().split())), reverse=True)
errors3 = sorted(list(map(int, input().split())), reverse=True)

last = True
for i in range(len(errors2)):
    if errors1[i] != errors2[i]:
        print(errors1[i])
        last = False
        break

if last == True:
    print(errors1[-1])

last = True
for i in range(len(errors3)):
    if errors2[i] != errors3[i]:
        print(errors2[i])
        last = False
        break

if last == True:
    print(errors2[-1])
