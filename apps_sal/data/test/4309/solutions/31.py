N = input()
if N[0] == N[1] == N[2]:
    print(int(N))
elif int(N[0]) < int(N[1]):
    x = (int(N[0]) + 1) * 100 + (int(N[0]) + 1) * 10 + int(N[0]) + 1
    print(x)
elif N[0] == N[1] and int(N[1]) > int(N[2]):
    x = int(N[0]) * 100 + int(N[0]) * 10 + int(N[0])
    print(x)
elif N[0] == N[1] and int(N[1]) < int(N[2]):
    x = (int(N[0]) + 1) * 100 + (int(N[0]) + 1) * 10 + int(N[0]) + 1
    print(x)
elif int(N[0]) > int(N[1]):
    x = int(N[0]) * 100 + int(N[0]) * 10 + int(N[0])
    print(x)
