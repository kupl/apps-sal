n = int(input())
for i in range(n,1000):
    x = list(str(i))
    if len(set(x)) == 1:
        print(i)
        break
