L = []
L.append(list(map(int, input().split())))
L.append(list(map(int, input().split())))
L.append(list(map(int, input().split())))
L = L[0] + L[1] + L[2]
print((L[0] + L[1] + L[3] + 1) % 2, end="")
print((L[1] + L[0] + L[2] + L[4] + 1) % 2, end="")
print((L[2] + L[1] + L[5] + 1) % 2)
print((L[0] + L[3] + L[6] + L[4] + 1) % 2, end="")
print((L[1] + L[4] + L[7] + L[3] + L[5] + 1) % 2, end="")
print((L[2] + L[5] + L[8] + L[4] + 1) % 2)
print((L[6] + L[7] + L[3] + 1) % 2, end="")
print((L[7] + L[8] + L[6] + L[4] + 1) % 2, end="")
print((L[8] + L[7] + L[5] + 1) % 2)
