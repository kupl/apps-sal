n, k = list(map(int,input().split()))
d = list(map(int,input().split()))

while n < 10**5:
    x = str(n)
    if all(int(i) not in d for i in x):
        print(n)
        return
    n += 1

