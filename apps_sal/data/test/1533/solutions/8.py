n = int(input())
s = set()
for i in range(n):
    x = input()
    print({True:"YES",False:"NO"}[x in s])
    s.add(x)

