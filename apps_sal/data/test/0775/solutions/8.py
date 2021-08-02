n, m, k = list(map(int, input().split()))
otv = set(input().split())
x = '1'
for _ in range(k):
    if x in otv:
        break
    o, p = input().split()
    if x == o:
        x = p
    elif x == p:
        x = o
print(x)
