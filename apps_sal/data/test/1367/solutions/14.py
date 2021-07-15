n = int(input())
ser = {x for x in range(1, n+1)}
serw = {int(x) for x in input().split()}
print(list(ser - serw)[0])

