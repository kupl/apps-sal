N = input()

if int(N) % sum(int(i) for i in N) == 0:
    print("Yes")
else:
    print("No")
