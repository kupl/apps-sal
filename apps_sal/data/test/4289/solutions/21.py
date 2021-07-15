n = int(input())
t, a = map(int,input().split())
h = list(map(int,input().split()))

atlist = []
for i in h:
    atlist.append(abs(a - (t - i * 0.006)))

print(atlist.index(min(atlist)) + 1)
