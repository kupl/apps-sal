(A1, A2, A3) = map(int, input().split())
a = []
a.append(abs(A2 - A1) + abs(A3 - A2))
a.append(abs(A2 - A3) + abs(A1 - A2))
a.append(abs(A1 - A2) + abs(A3 - A1))
a.append(abs(A1 - A3) + abs(A2 - A1))
a.append(abs(A3 - A1) + abs(A2 - A3))
a.append(abs(A3 - A2) + abs(A1 - A3))
print(min(a))
