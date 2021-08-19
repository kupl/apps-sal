n = int(input())
(T, A) = map(int, input().split())
h = list(map(int, input().split()))
a = []
for i in h:
    a.append(abs(A - (T - i * 0.006)))
print(a.index(min(a)) + 1)
