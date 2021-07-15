# ABC-106-C
S = input().rstrip()
K = int(input())


for s in S[:K]:
    if s != '1':
        print(s)
        return
print(1)
