n = int(input())
f = [1, 1]
for i in range(2, 20):
    f.append(f[i - 1] + f[i - 2])
for i in range(n):
    if(i + 1 in f):
        print("O", end="")
    else:
        print("o", end="")
