t = int(input())
for i in range(t):
    n = input()
    k = []
    for i in range(len(n)):
        if n[i] != "0":
            k.append(int(n[i])*10**(len(n)-i-1))
    print(len(k))
    print(*k)
