N, M = map(int, input().split())

if N == 1:
    lst = [str(i) for i in range(10)]

elif N == 2:
    lst = [str(i) for i in range(10, 100)]

else:
    lst = [str(i) for i in range(100, 1000)]

for j in range(M):
    s, c = map(int, input().split())
    lst = [i for i in lst if i[s-1] == str(c)]

if len(lst) == 0:
    print(-1)

else:
    print(lst[0])
