(N, A, B) = map(int, input().split())
a = list()
for i in range(N + 1):
    if A <= sum(map(int, str(i))) <= B:
        a.append(i)
print(sum(a))
