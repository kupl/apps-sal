N = int(input())
(T, A) = map(int, input().split())
H = [int(i) for i in input().split()]
temp = []
for i in H:
    temp.append(abs(A - (T - i * 0.006)))
min_ind = temp.index(min(temp))
print(min_ind + 1)
