N = int(input())
a = list(map(int,input().split()))

if not(1 in a):
    print(-1)
    return

l = []
min_num = 0
for i in a:
    if i == min_num + 1:
        l.append(i)
        min_num += 1

print(N-len(l))
