input()
A = sorted(int(x)for x in input().split())
s = sum(A)
input()
for q in map(int, input().split()):
    print(s - A[-q])
