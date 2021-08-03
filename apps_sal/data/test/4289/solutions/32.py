N = int(input())
T, A = map(float, input().split())
H = list(map(float, input().split()))
d = []
for i in H:
    d.append(abs(A - (T - i * 0.006)))
print(d.index(min(d)) + 1)
